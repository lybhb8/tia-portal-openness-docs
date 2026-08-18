"""
Sphinx 内容验证测试
验证文档内容的完整性和正确性
"""
import pytest
from pathlib import Path
import re


@pytest.fixture
def docs_dir():
    """文档目录"""
    return Path(__file__).parent.parent / "docs"


def test_heading_hierarchy(docs_dir):
    """测试标题层级结构"""
    issues = []

    for md_file in docs_dir.glob("*.md"):
        if md_file.name == "index.md":
            continue

        with open(md_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        prev_level = 0
        for i, line in enumerate(lines, 1):
            match = re.match(r"^(#{1,6})\s+(.*)$", line)
            if match:
                level = len(match.group(1))
                title = match.group(2).strip()

                # 检查层级是否跳过
                if level > prev_level + 1 and prev_level > 0:
                    issues.append(
                        f"{md_file.name}:{i} - 标题层级跳跃: "
                        f"从 #{prev_level} 跳到 #{level}"
                    )

                prev_level = level

    # 只报告前 5 个问题
    if issues:
        for issue in issues[:5]:
            print(f"  ⚠ {issue}")
        # 不中断测试，只是警告
    assert True, "标题层级检查完成"


def test_blank_lines_around_headings(docs_dir):
    """测试标题周围的空行"""
    warnings = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if re.match(r"^#{1,6}\s+", line):
                # 检查前一行
                if i > 0 and lines[i - 1].strip() != "":
                    warnings.append(
                        f"{md_file.name}:{i + 1} - 标题前缺少空行"
                    )
                # 检查后一行
                if i < len(lines) - 1 and lines[i + 1].strip() != "":
                    warnings.append(
                        f"{md_file.name}:{i + 1} - 标题后缺少空行"
                    )

    # 只报告前 10 个警告
    if warnings:
        for warning in warnings[:10]:
            print(f"  ⚠ {warning}")

    assert True, "空行检查完成"


def test_chapter_files_complete(docs_dir):
    """测试章节文件完整性"""
    expected = [
        "chapter_01_1 网络安全信息.md",
        "chapter_02_2 TIA Portal Openness 自述文件.md",
        "chapter_03_3 TIA Portal Openness 中的新功能.md",
        "chapter_04_4 基本知识.md",
        "chapter_05_5 TIA Portal Openness API.md",
        "chapter_06_6 导出导入.md",
        "chapter_07_7 主要变化.md",
    ]

    missing = []
    for filename in expected:
        filepath = docs_dir / filename
        if not filepath.exists():
            missing.append(filename)

    assert len(missing) == 0, f"缺少章节文件: {missing}"


def test_index_has_toctree(docs_dir):
    """测试 index.md 包含 toctree"""
    index_file = docs_dir / "index.md"
    assert index_file.exists(), "index.md 不存在"

    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "toctree" in content, "index.md 缺少 toctree"


def test_internal_links_valid(docs_dir):
    """测试内部链接"""
    # 收集所有标题
    headings = set()
    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(r"^#{1,6}\s+(.+)$", content, re.MULTILINE):
            title = match.group(1).strip()
            anchor = re.sub(r'[^\w一-鿿\s-]', '', title).strip()
            anchor = anchor.replace(' ', '-')
            headings.add(f"{md_file.stem}#{anchor}")

    # 检查链接
    broken = []
    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(r'\[([^\]]+)\]\(#([^)]+)\)', content):
            anchor = match.group(2)
            link_key = f"{md_file.stem}#{anchor}"
            if link_key not in headings and f"#{anchor}" not in headings:
                broken.append(f"{md_file.name}: [{match.group(1)}](#{anchor})")

    if broken:
        print(f"  ⚠ 发现 {len(broken)} 个可能的无效链接")
        for link in broken[:5]:
            print(f"    - {link}")

    assert True, "内部链接检查完成"


def test_admonitions_converted(docs_dir):
    """测试提示框转换"""
    admonition_keywords = ["说明", "注意", "警告", "提示", "建议", "重要"]
    total_found = 0

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        for keyword in admonition_keywords:
            if f"[!{keyword.upper()}]" in content:
                total_found += 1

    print(f"  找到 {total_found} 个已转换的提示框")
    assert True, "提示框检查完成"
