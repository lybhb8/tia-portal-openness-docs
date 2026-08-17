# 本地测试说明

本目录包含用于本地测试和验证文档构建的 Sphinx 测试文件。

## 测试文件列表

- `test_build.py` - Sphinx 文档构建测试
- `test_content.py` - 内容验证测试（标题层级、空行等）
- `test_links.py` - 链接检查测试
- `test_examples.py` - 代码示例测试
- `requirements.txt` - 测试依赖

## 运行测试

```bash
# 安装测试依赖
pip install -r tests/requirements.txt

# 运行所有测试
pytest tests/ -v

# 运行特定测试
pytest tests/test_build.py -v
pytest tests/test_content.py -v
pytest tests/test_links.py -v
pytest tests/test_examples.py -v

# 运行带日志的测试
pytest tests/ -v --tb=short

# 运行并生成覆盖率报告
pytest tests/ -v --cov=tests
```

## 本地构建文档

```bash
# 使用 Sphinx 构建 HTML
sphinx-build -b html docs/ _build/html/

# 构建 PDF
sphinx-build -b latex docs/ _build/latex/
cd _build/latex/ && make

# 使用 Makefile
make html
make pdf
```

## 测试覆盖范围

| 测试文件 | 测试内容 |
|---------|---------|
| `test_build.py` | Sphinx 构建、HTML 生成、章节文件 |
| `test_content.py` | 标题层级、空行格式、章节完整性、toctree、内部链接、提示框 |
| `test_links.py` | 内部锚点、外部链接、图片链接、相对路径 |
| `test_examples.py` | C# 代码块、注释、API 使用 |
