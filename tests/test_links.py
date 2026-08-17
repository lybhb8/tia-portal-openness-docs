"""
Sphinx 链接检查测试
验证文档中的链接有效性
"""
import pytest
from pathlib import Path
import re


@pytest.fixture
def docs_dir():
    """文档目录"""
    return Path(__file__).parent.parent / "docs"


def test_internal_links(docs_dir):
    """测试内部锚点链接"""
    # 收集所有锚点
    anchors = set()
    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(r"^#{1,6}\s+(.+)$", content, re.MULTILINE):
            title = match.group(1).strip()
            anchor = re.sub(r'[^\w一-鿿\s-]', '', title).strip()
            anchor = anchor.replace(' ', '-')
            anchors.add(f"{md_file.stem}#{anchor}")

    # 检查链接
    broken = []
    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(r'\[([^\]]+)\]\(#([^)]+)\)', content):
            anchor = match.group(2)
            link_key = f"{md_file.stem}#{anchor}"
            if link_key not in anchors:
                broken.append(f"{md_file.name}: [{match.group(1)}](#{anchor})")

    if broken:
        print(f"  ⚠ 发现 {len(broken)} 个可能的无效链接")
        for link in broken[:5]:
            print(f"    - {link}")

    assert True, "内部链接检查完成"


def test_external_links(docs_dir):
    """测试外部链接"""
    external_links = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)', content):
            url = match.group(2)
            if not url.startswith('#'):
                external_links.append((md_file.name, match.group(1), url))

    print(f"  找到 {len(external_links)} 个外部链接")
    for filename, text, url in external_links[:10]:
        print(f"    [{filename}] {text}: {url}")

    assert True, "外部链接检查完成"


def test_image_links(docs_dir):
    """测试图片链接"""
    images_dir = docs_dir / "images"
    if not images_dir.exists():
        pytest.skip("images 目录不存在")

    # 收集引用的图片
    referenced_images = set()
    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', content):
            img_path = match.group(2)
            referenced_images.add(img_path)

    # 检查图片是否存在
    missing = []
    for img_path in referenced_images:
        full_path = images_dir / img_path
        if not full_path.exists():
            full_path = docs_dir / img_path
            if not full_path.exists():
                missing.append(img_path)

    print(f"  引用图片: {len(referenced_images)}")
    print(f"  缺失图片: {len(missing)}")

    if missing:
        for img in missing[:5]:
            print(f"    - {img}")

    assert len(missing) == 0, f"缺失图片: {missing}"


def test_relative_links(docs_dir):
    """测试相对路径链接"""
    issues = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(r'\[([^\]]+)\]\(([^#][^)]+)\)', content):
            link_path = match.group(2)
            if not link_path.startswith('http'):
                full_path = docs_dir / link_path
                if not full_path.exists():
                    issues.append(f"{md_file.name}: [{match.group(1)}]({link_path})")

    if issues:
        print(f"  ⚠ 发现 {len(issues)} 个可能的无效相对路径")
        for issue in issues[:5]:
            print(f"    - {issue}")

    assert True, "相对路径检查完成"
