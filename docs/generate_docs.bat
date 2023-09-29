
REM Generate .rst files using sphinx-apidoc
sphinx-apidoc -o ./api ../src

REM Build the documentation using sphinx-build
sphinx-build -b html ./ ./_build

