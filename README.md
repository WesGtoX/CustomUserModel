<h1 align="center">
  <a href="https://github.com/WesGtoX/CustomUserModel">
    <img src=".github/logo.svg" alt="Custom User Mode" title="Custom User Mode" width="250px">
  </a>
</h1>

<p align="center">
  <a href="#about-the-project">About</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#technology">Technology</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#roadmap">Roadmap</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#how-to-contribute">Contributing</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wesgtox/CustomUserModel?style=plastic" />
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/wesgtox/CustomUserModel?style=plastic" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/wesgtox/CustomUserModel?style=plastic" />
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/wesgtox/CustomUserModel?style=plastic" />
  <img alt="License" src="https://img.shields.io/github/license/wesgtox/CustomUserModel?style=plastic" />
</p>


# Custom User Mode

Fully replace the username field with an email field for Django authentication.


## About the Project

This project is a customization in the Django user model.

Django's authentication by username has been completely replaced by the user's email.


## Technology 

This project was developed with the following technologies:

- [Python](https://www.python.org/)
- [Django Framework](https://www.djangoproject.com/)


## Getting Started

### Prerequisites

- [Python](https://www.python.org/)


### Install and Run

1. Clone the repository:
```bash
git clone https://github.com/WesGtoX/CustomUserModel.git
```
2. Create and activate a virtual enviroment:
```bash
python -m venv venv
source venv/bin/activate
```
3. Install the dependencies:
```bash
pip install -r requirements-dev.txt
```
4. Run migrations:
```bash
./manage.py makemigrations
./manage.py migrate
```
5. Create a superuser:
```bash
./manage.py createsuperuser
```
6. Run:
```bash
./manage.py runserver
```
7. To run tests:
```bash
./manage.py test
```


## Roadmap

See the [open issues](https://github.com/WesGtoX/CustomUserModel/issues) for a list of proposed features (and known issues).


## How to contribute

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch `git checkout -b feature/my-feature`.  
3. Commit your Changes `git commit -m 'feat: My new feature'`.  
4. Push to the Branch `git push origin feature/my-feature`.  
5. Open a Pull Request.  

After the merge of your pull request is done, you can delete your branch.  


## License

Distributed under the MIT License. See [LICENSE](LICENSE.md) for more information.

---

Made with ♥ by [Wesley Mendes](https://wesleymendes.com.br/) :wave:
