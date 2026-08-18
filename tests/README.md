# 本地测试说明

本目录包含用于本地测试和验证文档构建的测试文件。

## 测试文件列表

- `test_build.py` - 文档构建测试脚本
- `test_content.py` - 内容验证测试
- `test_links.py` - 链接检查测试
- `test_examples/` - 代码示例测试目录
- `requirements-test.txt` - 测试依赖

## 运行测试

```bash
# 安装测试依赖
pip install -r requirements-test.txt

# 运行所有测试
python test_build.py
python test_content.py
python test_links.py

# 或使用 pytest
pytest tests/ -v
```

## 本地构建文档

```bash
# 安装 Sphinx
pip install -r requirements.txt

# 构建 HTML
sphinx-build -b html docs/ _build/html/

# 构建 PDF (需要 LaTeX)
sphinx-build -b latex docs/ _build/latex/
cd _build/latex/ && make

# 使用 Makefile
make html
make pdf
```
