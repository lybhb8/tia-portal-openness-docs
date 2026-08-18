#!/usr/bin/env python3
"""
链接检查测试
检查所有内部和外部链接的有效性
"""

import os
import re
import sys
from pathlib import Path


def check_internal_links():
    """检查内部链接"""
    print("=" * 60)
    print("检查 1: 内部链接")
    print("=" * 60)

    # 收集所有可能的锚点
    anchors = set()
    docs_dir = Path("docs")

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 收集标题
        for match in re.finditer(r"^#{1,6}\s+(.+)$", content, re.MULTILINE):
            title = match.group(1).strip()
            # 生成可能的锚点
            anchor = re.sub(r'[^\w一-鿿\s-]', '', title).strip()
            anchor = anchor.replace(' ', '-')
            anchors.add(f"{md_file.stem}#{anchor}")
            anchors.add(f"#{anchor}")

    # 检查链接
    broken_links = []
    valid_links = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 查找所有锚点链接
        for match in re.finditer(r'\[([^\]]+)\]\(#([^)]+)\)', content):
            link_text = match.group(1)
            anchor = match.group(2)
            full_link = f"{md_file.stem}#{anchor}"

            if full_link in anchors or anchor in anchors:
                valid_links.append(f"{md_file.name}: {link_text}")
            else:
                broken_links.append(
                    f"{md_file.name}: [{link_text}](#{anchor})"
                )

    print(f"  有效链接: {len(valid_links)}")
    print(f"  无效链接: {len(broken_links)}")

    if broken_links:
        print("\n  可能无效的链接:")
        for link in broken_links[:10]:
            print(f"    - {link}")
        return False
    else:
        print("✓ 所有内部链接有效")
        return True


def check_external_links():
    """检查外部链接"""
    print("\n" + "=" * 60)
    print("检查 2: 外部链接")
    print("=" * 60)

    docs_dir = Path("docs")
    external_links = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 查找外部链接
        for match in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)', content):
            link_text = match.group(1)
            url = match.group(2)
            # 排除本地链接和锚点
            if not url.startswith('#') and '://' in url:
                external_links.append((md_file.name, link_text, url))

    print(f"  找到 {len(external_links)} 个外部链接")

    # 注意：不实际检查 URL 是否可达（需要网络）
    # 只显示链接列表供手动检查
    if external_links:
        print("\n  外部链接列表:")
        for filename, text, url in external_links[:20]:
            print(f"    [{filename}] {text}: {url}")

    print("✓ 外部链接检查完成 (请手动验证链接有效性)")
    return True


def check_image_links():
    """检查图片链接"""
    print("\n" + "=" * 60)
    print("检查 3: 图片链接")
    print("=" * 60)

    docs_dir = Path("docs")
    images_dir = docs_dir / "images"

    if not images_dir.exists():
        print("⚠ images 目录不存在")
        return True

    # 收集所有引用的图片
    referenced_images = set()
    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        for match in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', content):
            alt_text = match.group(1)
            img_path = match.group(2)
            referenced_images.add(img_path)

    # 检查图片是否存在
    missing_images = []
    for img_path in referenced_images:
        # 处理相对路径
        full_path = images_dir / img_path
        if not full_path.exists():
            # 尝试直接在 docs 目录下查找
            full_path = docs_dir / img_path
            if not full_path.exists():
                missing_images.append(img_path)

    print(f"  引用图片: {len(referenced_images)}")
    print(f"  缺失图片: {len(missing_images)}")

    if missing_images:
        print("\n  缺失的图片:")
        for img in missing_images[:10]:
            print(f"    - {img}")
        return False
    else:
        print("✓ 所有图片存在")
        return True


def check_relative_links():
    """检查相对路径链接"""
    print("\n" + "=" * 60)
    print("检查 4: 相对路径链接")
    print("=" * 60)

    docs_dir = Path("docs")
    issues = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 查找相对路径链接
        for match in re.finditer(r'\[([^\]]+)\]\(([^#][^)]+)\)', content):
            link_text = match.group(1)
            link_path = match.group(2)

            # 检查是否是相对路径
            if not link_path.startswith('http') and not link_path.startswith('#'):
                # 检查文件是否存在
                full_path = docs_dir / link_path
                if not full_path.exists():
                    issues.append(
                        f"{md_file.name}: [{link_text}]({link_path})"
                    )

    if issues:
        print(f"⚠ 发现 {len(issues)} 个可能的无效相对路径")
        for issue in issues[:5]:
            print(f"  - {issue}")
        return True
    else:
        print("✓ 相对路径检查完成")
        return True


def main():
    """主测试函数"""
    print("\n" + "=" * 60)
    print("TIA Portal Openness 链接检查测试")
    print("=" * 60 + "\n")

    results = []

    results.append(("内部链接", check_internal_links()))
    results.append(("外部链接", check_external_links()))
    results.append(("图片链接", check_image_links()))
    results.append(("相对路径", check_relative_links()))

    # 汇总
    print("\n" + "=" * 60)
    print("测试结果汇总")
    print("=" * 60)

    passed = sum(1 for _, r in results if r)
    print(f"通过: {passed}/{len(results)}")

    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
