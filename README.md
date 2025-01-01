# Miniature-Spider

A scrapy-powered spider that parses miniature websites.

## Prerequisites

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

You will need to install some libs in order to run any spider. To install them, run the following command:

```bash
pip install -r requirements.txt
```

You also will need to install docker && docker-compose.

## Creating and Using a Virtual Environment (venv)

It is recommended to use a virtual environment to isolate the dependencies of this project from your system's global Python installation. Here's how you can create and use a virtual environment:

### Step 1: Create a Virtual Environment

Run the following command in the root directory of your project to create a virtual environment named `venv`:

```bash
python3 -m venv venv
```

### Step 2: Activate the Virtual Environment

- On **UNIX or MacOS**, run:

  ```bash
  source venv/bin/activate
  ```

- On **Windows**, run:

  ```bash
  .\venv\Scripts\activate
  ```

After activation, your shell prompt should change to indicate that the virtual environment is active.

### Step 3: Install Dependencies

With the virtual environment active, install the project dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Deactivate the Virtual Environment

When you are done working in the virtual environment, deactivate it by running:

```bash
deactivate
```

## Run the Project

Before executing anything, keep in mind that this execution may take days:

```bash
docker-compose up -d

cd miniature

scrapy crawl zack
```

If your system (I assume it is UNIX) does not recognize the command "scrapy" add it to your path:

```bash
PATH="${PATH}:${HOME}/.local/bin"
```


## Run the project

Before executing anything, keep in mind that this execution may take days:

```bash
docker-compose up -d

cd miniature

scrapy crawl zack
```

If your system (I assume it is UNIX) does not recognize the command "scrapy" add it to your path:

```bash
PATH="${PATH}:${HOME}/.local/bin"
```

## Built With

* [Scrapy](https://scrapy.org/)
* [Docker](https://www.docker.com/)
* [Privoxy](https://www.privoxy.org/)
* [Tor](https://www.torproject.org/)

## Authors

* **Diego Dominguez**   <a href="https://twitter.com/DGlez1111" target="_blank">
    <img alt="Twitter: DGlez1111" src="https://img.shields.io/twitter/follow/DGlez1111.svg?style=social" />
  </a>

## MIT License

Copyright (c) 2025 Diego Domínguez González

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
