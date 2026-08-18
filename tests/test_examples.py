# -*- coding: utf-8 -*-
"""
TIA Portal Openness 示例代码测试
测试文档中的 C# 代码示例
"""

import re
import sys
from pathlib import Path


def extract_code_blocks():
    """从文档中提取代码块"""
    docs_dir = Path("docs")
    code_blocks = []

    for md_file in docs_dir.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 查找 C# 代码块
        pattern = r'```csharp\s*\n(.*?)\n```'
        for match in re.finditer(pattern, content, re.DOTALL):
            code = match.group(1).strip()
            code_blocks.append({
                'file': md_file.name,
                'code': code,
                'lines': code.split('\n')
            })

    return code_blocks


def check_syntax(code_blocks):
    """检查代码语法"""
    print("=" * 60)
    print("检查代码语法")
    print("=" * 60)

    issues = []
    for block in code_blocks:
        code = block['code']

        # 检查基本语法结构
        if 'using' in code:
            # 检查 using 语句
            using_lines = [l for l in code.split('\n') if l.strip().startswith('using ')]
            if using_lines:
                print(f"  [{block['file']}] 找到 {len(using_lines)} 个 using 语句")

        # 检查大括号匹配
        open_braces = code.count('{')
        close_braces = code.count('}')
        if open_braces != close_braces:
            issues.append(
                f"{block['file']}: 大括号不匹配 "
                f"({open_braces} 个 {{ vs {close_braces} 个 }})"
            )

    if issues:
        print("\n❌ 发现语法问题:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("✓ 代码语法检查通过")
        return True


def check_api_usage():
    """检查 API 使用情况"""
    print("\n" + "=" * 60)
    print("检查 API 使用")
    print("=" * 60)

    # 检查是否使用了正确的命名空间
    expected_namespaces = [
        'Siemens.Engineering',
        'Siemens.Engineering.Automation',
        'System.IO',
    ]

    code_blocks = extract_code_blocks()
    found_namespaces = set()

    for block in code_blocks:
        for ns in expected_namespaces:
            if ns in block['code']:
                found_namespaces.add(ns)

    print(f"  找到 {len(found_namespaces)} 个命名空间:")
    for ns in sorted(found_namespaces):
        print(f"    - {ns}")

    print("✓ API 使用检查完成")
    return True


def check_documentation():
    """检查代码注释"""
    print("\n" + "=" * 60)
    print("检查代码注释")
    print("=" * 60)

    code_blocks = extract_code_blocks()
    documented = 0
    total = len(code_blocks)

    for block in code_blocks:
        if '///' in block['code'] or '//' in block['code'] or '/*' in block['code']:
            documented += 1

    print(f"  有注释的代码块: {documented}/{total}")

    if total > 0:
        ratio = documented / total * 100
        print(f"  注释覆盖率: {ratio:.1f}%")

    print("✓ 注释检查完成")
    return True


def main():
    """主测试函数"""
    print("\n" + "=" * 60)
    print("TIA Portal Openness 示例代码测试")
    print("=" * 60 + "\n")

    code_blocks = extract_code_blocks()
    print(f"从文档中提取了 {len(code_blocks)} 个代码块\n")

    results = []
    results.append(("语法检查", check_syntax(code_blocks)))
    results.append(("API 使用", check_api_usage()))
    results.append(("代码注释", check_documentation()))

    # 汇总
    print("\n" + "=" * 60)
    print("测试结果汇总")
    print("=" * 60)

    passed = sum(1 for _, r in results if r)
    print(f"通过: {passed}/{len(results)}")

    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
