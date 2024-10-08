import subprocess

# Upgrade pip first
subprocess.check_call(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])

# List of required packages
packages = [
    'absl-py==1.4.0',
    'anyio==3.6.2',
    'astunparse==1.6.3',
    'cachetools==5.3.0',
    'certifi==2022.12.7',
    'charset-normalizer==3.1.0',
    'click==8.1.3',
    'colorama==0.4.6',
    'contourpy==1.0.7',
    'cycler==0.11.0',
    'fastapi==0.95.1',
    'flatbuffers==23.3.3',
    'fonttools==4.39.3',
    'gast==0.4.0',
    'google-auth==2.17.3',
    'google-auth-oauthlib==1.0.0',
    'google-pasta==0.2.0',
    'grpcio==1.54.0',
    'h11==0.14.0',
    'h5py==3.8.0',
    'idna==3.4',
    'jax==0.4.8',
    'joblib==1.2.0',
    'keras==2.12.0',
    'kiwisolver==1.4.4',
    'libclang==16.0.0',
    'Markdown==3.4.3',
    'MarkupSafe==2.1.2',
    'matplotlib==3.7.1',
    'ml-dtypes==0.1.0',
    'nltk==3.8.1',
    'numpy==1.23.5',
    'oauthlib==3.2.2',
    'opt-einsum==3.3.0',
    'packaging==23.1',
    'Pillow==9.5.0',
    'protobuf==4.22.3',
    'pyasn1==0.5.0',
    'pyasn1-modules==0.3.0',
    'pydantic==1.10.7',
    'pyparsing==3.0.9',
    'python-dateutil==2.8.2',
    'pytz==2023.3',
    'regex==2023.5.4',
    'requests==2.29.0',
    'requests-oauthlib==1.3.1',
    'rsa==4.9',
    'scipy==1.10.1',
    'six==1.16.0',
    'sniffio==1.3.0',
    'starlette==0.26.1',
    'tensorboard==2.12.2',
    'tensorboard-data-server==0.7.0',
    'tensorboard-plugin-wit==1.8.1',
    'tensorflow==2.12.0',
    'tensorflow-estimator==2.12.0',
    'tensorflow-intel',
    'tensorflow-io-gcs-filesystem==0.31.0',
    'termcolor==2.3.0',
    'tqdm==4.65.0',
    'typing_extensions==4.5.0',
    'urllib3==1.26.15',
    'uvicorn==0.22.0',
    'Werkzeug==2.3.3',
    'wrapt==1.14.1'
]

# Install required packages
for package in packages:
    subprocess.check_call(['pip', 'install', package])

subprocess.check_call(['python3', '-m', 'nltk.downloader', 'stopwords'])

# Install NLTK data
import nltk
nltk.download('punkt')
nltk.download('wordnet')
