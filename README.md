# How to install, test and use the application

```bash
docker build -t zmbner .
docker run -v ./wheel:/zmbner/wheel -it zmbner /bin/bash
pip install -e .
pytest
python setup.py bdist_wheel
cp dist/zmbner-0.1.0-py3-none-any.whl wheel
```