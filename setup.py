from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'User management authentiation'

try:
    # read the contents of README file
    from pathlib import Path
    this_directory = Path(__file__).parent
    LONG_DESCRIPTION = (this_directory / "README.md").read_text()
except:
    LONG_DESCRIPTION = 'User management authentication and authorization for FastAPI using AWS Cognito service'

# Setting up
setup(
        name="ofry-fasatpi-auth-cognito", 
        version=VERSION,
        author="Ofry Makdasy",
        author_email="ofry.makdsy@tech-19.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[
            'aiofiles==0.5.0',
            'aniso8601==7.0.0',
            'anyio==3.6.2',
            'appdirs==1.4.4',
            'async-exit-stack==1.0.1',
            'async-generator==1.10',
            'atomicwrites==1.4.0',
            'attrs==20.3.0',
            'black==20.8b1',
            'certifi==2020.12.5',
            'chardet==4.0.0',
            'click==7.1.2',
            'colorama==0.4.4',
            'dnspython==2.1.0',
            'ecdsa==0.18.0',
            'email-validator==1.1.2',
            'fastapi==0.63.0',
            'graphene==2.1.8',
            'graphql-core==2.3.2',
            'graphql-relay==2.0.1',
            'greenlet==1.0.0',
            'h11==0.14.0',
            'httpcore==0.16.2',
            'httpx==0.23.1',
            'idna==2.10',
            'iniconfig==1.1.1',
            'isort==5.8.0',
            'itsdangerous==1.1.0',
            'Jinja2==2.11.3',
            'MarkupSafe==1.1.1',
            'mypy-extensions==0.4.3',
            'orjson==3.5.2',
            'packaging==20.9',
            'pathspec==0.8.1',
            'pluggy==0.13.1',
            'promise==2.3',
            'psycopg2==2.8.6',
            'py==1.10.0',
            'pyasn1==0.4.8',
            'pybase64==1.2.3',
            'pydantic==1.8.2',
            'pydantic-sqlalchemy==0.0.9',
            'PyJWT==2.6.0',
            'pyparsing==2.4.7',
            'pytest==6.2.3',
            'pytest-dependency==0.5.1',
            'python-decouple==3.4',
            'python-dotenv==0.17.0',
            'python-jose==3.3.0',
            'python-multipart==0.0.5',
            'PyYAML==5.4.1',
            'regex==2021.4.4',
            'requests==2.25.1',
            'rfc3986==1.5.0',
            'rsa==4.9',
            'Rx==1.6.1',
            'six==1.15.0',
            'sniffio==1.3.0',
            'SQLAlchemy==1.4.11',
            'starlette==0.13.6',
            'toml==0.10.2',
            'typed-ast==1.4.3',
            'typing-extensions==3.7.4.3',
            'ujson==3.2.0',
            'urllib3==1.26.5',
            'uvicorn==0.13.4',
            'watchgod==0.7',
            'websockets==9.1',
        ],
        
        keywords=['python', 'first package' , 'fastapi' , 'cognito' , 'jwt'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)