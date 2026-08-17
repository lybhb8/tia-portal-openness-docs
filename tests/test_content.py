#!/usr/bin/env python3
"""
内容验证测试
检查文档内容的完整性和正确性
"""

import os
import re
import sys
from pathlib import Path


def check_heading_hierarchy():
    """检查标题层级"""
    print("=" * 60)
    print("检查 1: 标题层级结构")
    print("=" * 60)

    issues = []
    docs_dir = Path("docs")

    for md_file in docs_dir.glob("*.md"):
        if md_file.name == "index.md":
            continue

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.split("\n")
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
                        f"从 #{prev_level} 跳到 #{level} ('{title[:30]}...')"
                    )

                prev_level = level

    if issues:
        print(f"❌ 发现 {len(issues)} 个标题层级问题")
        for issue in issues[:5]:
            print(f"  - {issue}")
        return False
    else:
        print("✓ 标题层级结构正确")
        return True


def check_blank_lines():
    """检查标题周围的空行"""
    print("\n" + "=" * 60)
    print("检查 2: 标题周围空行")
    print("=" * 60)

    issues = []
    docs_dir = Path("docs")

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if re.match(r"^#{1,6}\s+", line):
                # 检查前一行是否为空
                if i > 0 and lines[i - 1].strip() != "":
                    issues.append(
                        f"{md_file.name}:{i + 1} - 标题前缺少空行"
                    )
                # 检查后一行是否为空
                if i < len(lines) - 1 and lines[i + 1].strip() != "":
                    issues.append(
                        f"{md_file.name}:{i + 1} - 标题后缺少空行"
                    )

    if issues:
        print(f"⚠ 发现 {len(issues)} 个空行问题 (建议修复)")
        for issue in issues[:10]:
            print(f"  - {issue}")
        return True  # 只是建议，不中断
    else:
        print("✓ 标题空行格式正确")
        return True


def check_internal_links():
    """检查内部链接"""
    print("\n" + "=" * 60)
    print("检查 3: 内部链接有效性")
    print("=" * 60)

    # 收集所有标题
    headings = {}
    docs_dir = Path("docs")

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        for match in re.finditer(r"^#{1,6}\s+(.+)$", content, re.MULTILINE):
            title = match.group(1).strip()
            # 生成锚点
            anchor = re.sub(r'[^\w一-鿿\s-]', '', title).strip()
            anchor = anchor.replace(' ', '-')
            headings[f"{md_file.stem}#{anchor}"] = md_file.name

    # 检查链接
    broken_links = []
    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 查找锚点链接
        for match in re.finditer(r'\[([^\]]+)\]\(#([^)]+)\)', content):
            link_text = match.group(1)
            anchor = match.group(2)
            link_key = f"{md_file.stem}#{anchor}"

            if link_key not in headings and anchor not in headings:
                broken_links.append(
                    f"{md_file.name}: [{link_text}](#{anchor}) - 可能无效的锚点"
                )

    if broken_links:
        print(f"⚠ 发现 {len(broken_links)} 个可能的无效链接")
        for link in broken_links[:5]:
            print(f"  - {link}")
        return True
    else:
        print("✓ 内部链接检查完成")
        return True


def check_chapter_files():
    """检查章节文件"""
    print("\n" + "=" * 60)
    print("检查 4: 章节文件完整性")
    print("=" * 60)

    expected_files = [
        "chapter_01_1 网络安全信息.md",
        "chapter_02_2 TIA Portal Openness 自述文件.md",
        "chapter_03_3 TIA Portal Openness 中的新功能.md",
        "chapter_04_4 基本知识.md",
        "chapter_05_5 TIA Portal Openness API.md",
        "chapter_06_6 导出导入.md",
        "chapter_07_7 主要变化.md",
    ]

    missing = []
    for filename in expected_files:
        filepath = Path("docs") / filename
        if not filepath.exists():
            missing.append(filename)

    if missing:
        print(f"❌ 缺少 {len(missing)} 个章节文件:")
        for f in missing:
            print(f"  - {f}")
        return False
    else:
        print(f"✓ 所有 {len(expected_files)} 个章节文件存在")
        return True


def check_admonitions():
    """检查提示框转换"""
    print("\n" + "=" * 60)
    print("检查 5: 提示框 (Admonitions) 转换")
    print("=" * 60)

    admonition_keywords = ["说明", "注意", "警告", "提示", "建议", "重要"]
    found_admonitions = []

    docs_dir = Path("docs")
    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        for keyword in admonition_keywords:
            if keyword in content:
                # 检查是否已转换为 callout 格式
                if f"> [!{keyword.upper()}]" in content:
                    found_admonitions.append(f"{md_file.name}: {keyword}")

    print(f"  找到 {len(found_admonitions)} 个已转换的提示框")
    print("✓ 提示框检查完成")
    return True


def main():
    """主测试函数"""
    print("\n" + "=" * 60)
    print("TIA Portal Openness 文档内容验证测试")
    print("=" * 60 + "\n")

    results = []

    results.append(("标题层级", check_heading_hierarchy()))
    results.append(("空行格式", check_blank_lines()))
    results.append(("内部链接", check_internal_links()))
    results.append(("章节文件", check_chapter_files()))
    results.append(("提示框", check_admonitions()))

    # 汇总
    print("\n" + "=" * 60)
    print("测试结果汇总")
    print("=" * 60)

    passed = sum(1 for _, r in results if r)
    print(f"通过: {passed}/{len(results)}")

    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
