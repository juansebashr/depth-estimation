<div id="top"></div> 

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/juansebashr/kiwibot-depth-estimation">
    <img src="docs/images/kiwibotLogo.png" alt="Logo" width="200" height="200">
  </a>
<h3 align="center">Monocular Depth Estimation - Entry Project</h3>

<p align="center">
    Training of different monocular depth prediction models in a dataset of cameras and sensors belonging to a 
    Kiwibot robot.
    <br />
    <br />
    <a href="https://github.com/juansebashr/kiwibot-depth-estimation/pulls">Make a Pull Request</a>
    ·
    <a href="https://github.com/juansebashr/kiwibot-depth-estimation/issues">Report Bug</a>
    ·
    <a href="https://github.com/juansebashr/kiwibot-depth-estimation/issues">Request Feature</a>
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
    <li><a href="#Get the models">Outputs</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

This project is the final step of the Kiwibot entry process, where the tasks were:

1. Build a model for depth estimation using all 4 cameras. The model should process the 4
  cameras at the time and output the corresponding 4 depth maps
2. [Extra]: Build a model like in (1), but now include time in the model (take into account a
   sequence of consecutive images at a time)

To accomplish that, 3 models were trained, the first was a U-Net trained in Tensorflow (Keras) to provide a
first grasp of the task getting good results. Then the MiDaS model from [this](https://arxiv.org/abs/1907.01341) 
paper was fine-tuned on the datasets, greatly improving the results.

Finally, a Conv-LSTM based U-Net from [this](paper) was implemented, but due to the size of the network the training
was very slow on a 12Gb GTX-3060. 


<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Tensorflow](https://www.tensorflow.org/)
* [Pytorch](https://pytorch.org/)
* [ONNX](https://onnx.ai/)
* Some common libraries of data science in python

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

### Running the code

Finally, you can run the code using the following command:

   ```sh
   python src/predict_depth.py --model midas --frames 4 --gpu true
   ```

There are 3 arguments to run the code: 

* `model`: Select the model to use, either midas or unet
* `frames`: The number of frames that will be predicted from the 4 cameras of the original data
* `gpu`: Either true or false, selects to run ONNX runtime in either a GPU or CPU

### Checking the training code

All the training code and history for all 3 models are available in the notebooks directory. Each notebook has the 
explanation of every part of the training process

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- OUTPUTS EXAMPLES -->

## Get the models

To get the data, you have to install dvc (follow [this](https://dvc.org/doc/install) link) and configure the remote
bucket where the data is stored.

```
dvc remote add --default myremote gdrive://1WGZtOysGV925-CFLEazZNTBzGQwwBBzo
```
and then downloading using the following command:

`dvc pull`

<!-- CONTACT -->

## Contact

Sebastián Hernández Reyes - juansebashr@gmail.com

Github profile: https://github.com/juansebashr

LinkedIn profile: https://www.linkedin.com/in/sebastian-hernandez-reyes-76a0a8148/

<!-- Template developed by the ML Team :D-->

<p align="right">(<a href="#top">back to top</a>)</p>
