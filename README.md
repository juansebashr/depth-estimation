<div id="top"></div> 

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/juansebashr/kiwibot-depth-estimation">
    <img src="docs/images/kiwibotLogo.png" alt="Logo" width="200" height="200">
  </a>
<h3 align="center">Monocular Depth Estimation - Entry Project</h3>

  <p align="center">
    A little description of your project
    <br />
    <a href="https://a_url_that_has_documentation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/chiper-inc/your_repo_name/pulls">Make a Pull Request</a>
    ·
    <a href="https://github.com/chiper-inc/your_repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/chiper-inc/your_repo_name/issues">Request Feature</a>
  </p>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#outputs">Outputs</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

A more detailed description of the project, what it does, what it was built for, to which STT or cell it belongs (
last-mile, supply, pricing, etc), what it uses as input and what as output

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* Another library or technology that you think is useful to put

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

To run this code, it's recommended that you start a new python environment (Using [venv](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)
or [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)) and install the
packages in the requirements.txt file

  ```sh
  pip install -r requirements.txt
  ```

### Environment variables

To run this project, you will need to set environment variables, this can be done using a `.env` file and
a plugin for your IDE, or if you're using conda or venv, you can set the environment variables right into the
terminal.  
These are the environment variables needed to run the code:
```
CREDENTIALS_PATH=path/to/credentials.json 
ENVIRONMENT 
LOGGING_ENV
add the variables you need, remember that must be in upper case and not use special characters
```


The `CREDENTIALS_PATH` variable is the path to the credentials file for the Google Cloud Platform, if you don't have it
ask for it to your leader or the owner of this repo, is important to set this variable as the global path in your
machine. The `LOGGING_ENV` variable is used to determine the type of logging your code is using, if you are running on any
cloud environment use `gcp` otherwise use `develop`.

The environment variables for develop and staging are [here](https://github.com/chiper-inc/deployments-beta-stag/tree/main/cronjobs) 
and the environment variables for production are [here](https://github.com/chiper-inc/deployments-prod/tree/main/cronjobs/data-science), 
search for the repo/cronjob name and look the `variables.properties` file.

### Running the code

Finally, you can run the code using the following command:

   ```sh
   python src/main/predict_depth.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- OUTPUTS EXAMPLES -->

## Outputs

The outputs of the cron are the following:

* Here you specify with full details the expected output of the cron, if is a BigQuery table, a database or something
  like it put the direction of the table in each environment. Please be as specific and detailed as possible.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Your name and your mail

Project Link: [https://github.com/chiper-inc/your_repo_name](https://github.com/chiper-inc/your_repo_name)

<!-- Template developed by the ML Team :D-->

<p align="right">(<a href="#top">back to top</a>)</p>
