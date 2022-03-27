<div id="top"></div>


<!-- PROJECT SHIELDS -->
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![The Unlicense License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">e-istichara Monitor</h3>

  <p align="center">
    <br />
    <a href="https://github.com/iyedg/e_istichara_monitor/issues">Report Bug</a>
    ·
    <a href="https://github.com/iyedg/e_istichara_monitor/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple Python Script that was written to monitor the progress of
official indicators of the Tunisian National Consultation of 2022. The official website https://www.e-istichara.tn relies on a JSON API. This script calls that API periodically to save the indicators displayed on the website. As of now, the consultation was concluded on the 20<sup>th</sup> of March, 2022, therefore this code is shared for posterity's sake. The actual data collected is available upon request.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [requests](https://docs.python-requests.org/en/latest/)
* [tenacity](https://tenacity.readthedocs.io/en/latest/)
* [schedule](https://schedule.readthedocs.io/en/stable/)
* [poetry](https://python-poetry.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



The environment necesseary for running this project requires at least Python 3.10 . I recommend using a tool like `pyenv` to manage your Python versions.

If you are using `poetry`, simply change your directory to the root of this project, and run the following command

```sh
poetry install
```

which will manage your virtual environment and the installation of the libraries inside of it for you.

If you wish to use `pip` instead, please make sure to create a separate virtual environment and then run the following command **in the activated virtual environment**

```sh
python -m pip install -r requirements.txt
```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run this tool, simply run the following command.

```sh
python e_istichara_monitor/istichara.py
```



<p align="right">(<a href="#top">back to top</a>)</p>



## Requesting the Data

If you wish to access the data collected by this script, please send me an email on `contact@iyedg.me`. If you create something using this data, please credit this work properly.



<p align="right">(<a href="#top">back to top</a>)</p>

## Where has this been used ?

A list of places where the data generated from this script was used:

* [الاستشارة الالكترونيّة: الرئيس يستشير نفسه](https://www.albawsala.com/ar/publications/articles/20224977)


<!-- LICENSE -->
## Licenses

### Code

Distributed under the Unlicense License. See `UNLICENSE.txt` for more information.

### Data

<p xmlns:cc="http://creativecommons.org/ns#" ><a rel="cc:attributionURL" href="https://github.com/iyedg/e_istichara_monitor">The data collected by this work</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://iyedg.me">Iyed Ghedamsi</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"></a></p>


For a Human readable version of this license see [this link](https://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1). See `BY-NC.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/iyedg/e_istichara_monitor.svg?style=for-the-badge
[contributors-url]: https://github.com/iyedg/e_istichara_monitor/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/iyedg/e_istichara_monitor.svg?style=for-the-badge
[forks-url]: https://github.com/iyedg/e_istichara_monitor/network/members
[stars-shield]: https://img.shields.io/github/stars/iyedg/e_istichara_monitor.svg?style=for-the-badge
[stars-url]: https://github.com/iyedg/e_istichara_monitor/stargazers
[issues-shield]: https://img.shields.io/github/issues/iyedg/e_istichara_monitor.svg?style=for-the-badge
[issues-url]: https://github.com/iyedg/e_istichara_monitor/issues
[license-shield]: https://img.shields.io/github/license/iyedg/e_istichara_monitor.svg?style=for-the-badge
[license-url]: https://github.com/iyedg/e_istichara_monitor/blob/master/UNLICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/iyed-ghedamsi
[product-screenshot]: images/screenshot.png

