<p align="center"><img width="65%" src="docs/source/_static/img/evalai_logo.png"/></p>

------------------------------------------------------------------------------------------

[![Join the chat at https://gitter.im/Cloud-CV/EvalAI](https://badges.gitter.im/Cloud-CV/EvalAI.svg)](https://gitter.im/Cloud-CV/EvalAI?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/Cloud-CV/EvalAI.svg?branch=master)](https://travis-ci.org/Cloud-CV/EvalAI)
[![Coverage Status](https://coveralls.io/repos/github/Cloud-CV/EvalAI/badge.svg)](https://coveralls.io/github/Cloud-CV/EvalAI)
[![Requirements Status](https://requires.io/github/Cloud-CV/EvalAI/requirements.svg?branch=master)](https://requires.io/github/Cloud-CV/EvalAI/requirements/?branch=master)
[![Code Health](https://landscape.io/github/Cloud-CV/EvalAI/master/landscape.svg?style=flat)](https://landscape.io/github/Cloud-CV/EvalAI/master)
[![Code Climate](https://codeclimate.com/github/Cloud-CV/EvalAI/badges/gpa.svg)](https://codeclimate.com/github/Cloud-CV/EvalAI)
[![Documentation Status](https://readthedocs.org/projects/markdown-guide/badge/?version=latest)](http://evalai.readthedocs.io/en/latest/)

EvalAI is an open source platform for evaluating and comparing machine learning (ML) and artificial intelligence (AI) algorithms at scale. 

In recent years, it has become increasingly difficult to compare an algorithm solving a given task with other existing approaches. These comparisons suffer from minor differences in algorithm implementation, use of non-standard dataset splits and different evaluation metrics. By providing a central leaderboard and submission interface, we make it easier for researchers to reproduce the results mentioned in the paper and perform reliable & accurate quantitative analysis. By providing swift and robust backends based on map-reduce frameworks that speed up evaluation on the fly, EvalAI aims to make it easier for researchers to reproduce results from technical papers and perform reliable and accurate analyses.

## Features

- **Custom evaluation protocols and phases**: We allow creation of an arbitrary number of evaluation phases and dataset splits, compatibility using any programming language, and organizing results in both public and private leaderboards.

- **Remote evaluation**: Certain large-scale challenges need special compute capabilities for evaluation. If the challenge needs extra computational power, challenge organizers can easily add their own cluster of worker nodes to process participant submissions while we take care of hosting the challenge, handling user submissions, and maintaining the leaderboard.

- **Evaluation inside environments**: EvalAI lets participants submit code for their agent in the form of docker images which are evaluated against test environments on the evaluation server. During evaluation, the worker fetches the image, test environment, and the model snapshot and spins up a new container to perform evaluation.

- **CLI support**: [evalai-cli](https://github.com/Cloud-CV/evalai-cli) is designed to extend the functionality of the EvalAI web application to your command line to make the platform more accessible and terminal-friendly.

- **Portability**: EvalAI is designed with keeping in mind scalability and portability of such a system from the very inception of the idea. Most of the components rely heavily on open-source technologies – Docker, Django, Node.js, and PostgreSQL.

- **Faster evaluation**: We warm-up the worker nodes at start-up by importing the challenge code and pre-loading the dataset in memory. We also split the dataset into small chunks that are simultaneously evaluated on multiple cores. These simple tricks result in faster evaluation and reduces the evaluation time by an order of magnitude in some cases.

## Platform Comparison
|          Features          |          OpenML          |         TopCoder         |          Kaggle          |          CrowdAI         |          ParlAI          |          Codalab         |       EvalAI       |
|:--------------------------:|:------------------------:|:------------------------:|:------------------------:|:------------------------:|:------------------------:|:------------------------:|:------------------:|
|    AI challenge hosting    | :heavy_multiplication_x: |    :white_check_mark:    |    :white_check_mark:    |    :white_check_mark:    | :heavy_multiplication_x: |    :white_check_mark:    | :white_check_mark: |
|       Custom metrics       | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |    :white_check_mark:    |    :white_check_mark:    |    :white_check_mark:    | :white_check_mark: |
|   Multiple phases/splits   | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |    :white_check_mark:    | :heavy_multiplication_x: |    :white_check_mark:    | :white_check_mark: |
|         Open source        |    :white_check_mark:    | :heavy_multiplication_x: | :heavy_multiplication_x: |    :white_check_mark:    |    :white_check_mark:    |    :white_check_mark:    | :white_check_mark: |
|      Remote evaluation     | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |    :white_check_mark:    |    :white_check_mark:    | :white_check_mark: |
|      Human evaluation      | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |    :white_check_mark:    | :heavy_multiplication_x: | :white_check_mark: |
| Evaluation in Environments | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |    :white_check_mark:    | :heavy_multiplication_x: | :heavy_multiplication_x: | :white_check_mark: |

## Goal

Our ultimate goal is to build a centralized platform to host, participate and collaborate in AI challenges organized around the globe and we hope to help in benchmarking progress in AI.

## Installation instructions

Setting up EvalAI on your local machine is really easy. You can setup EvalAI using docker:
The steps are:

1. Install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/) on your machine.

2. Get the source code on to your machine via git.

    ```shell
    git clone https://github.com/Cloud-CV/EvalAI.git evalai && cd evalai
    ```

3. Build and run the Docker containers. This might take a while.

    ```
    docker-compose up --build
    ```

4. That's it. Open web browser and hit the url [http://127.0.0.1:8888](http://127.0.0.1:8888). Three users will be created by default which are listed below -
    
    **SUPERUSER-** username: `admin` password: `password`  
    **HOST USER-** username: `host` password: `password`  
    **PARTICIPANT USER-** username: `participant` password: `password`

If you are facing any issue during installation, please see our [common errors during installation page](https://evalai.readthedocs.io/en/latest/faq(developers).html#common-errors-during-installation).

## Citing EvalAI
If you are using EvalAI for hosting challenges, please cite the following technical report:

```
@article{EvalAI,
    title   =  {EvalAI: Towards Better Evaluation Systems for AI Agents},
    author  =  {Deshraj Yadav and Rishabh Jain and Harsh Agrawal and Prithvijit
                Chattopadhyay and Taranjeet Singh and Akash Jain and Shiv Baran
                Singh and Stefan Lee and Dhruv Batra},
    year    =  {2019},
    volume  =  arXiv:1902.03570
}
```
<p>
    <a href="https://arxiv.org/abs/1902.03570"><img src="docs/source/_static/img/evalai-paper.jpg"/></a>
</p>

## Team

EvalAI is currently maintained by [Deshraj Yadav](https://deshraj.github.io) and [Rishabh Jain](https://rishabhjain2018.github.io/). A non-exhaustive list of other major contributors includes: [Akash Jain](http://www.jainakash.in/), [Taranjeet Singh](http://taranjeet.github.io/), [Shiv Baran Singh](http://www.shivbaran.in/), [Harsh Agarwal](https://dexter1691.github.io/), [Prithvijit Chattopadhyay](https://prithv1.github.io/), [Devi Parikh](https://www.cc.gatech.edu/~parikh/) and [Dhruv Batra](https://www.cc.gatech.edu/~dbatra/).

## Contributors

Thanks goes to these wonderful people
([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/jfmengels"><img src="https://avatars.githubusercontent.com/u/3869412?v=3" width="100px;" alt="Jeroen Engels"/><br /><sub><b>Jeroen Engels</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jfmengels" title="Code">💻</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jfmengels" title="Documentation">📖</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jfmengels" title="Tests">⚠️</a></td>
    <td align="center"><a href="http://kentcdodds.com/"><img src="https://avatars.githubusercontent.com/u/1500684?v=3" width="100px;" alt="Kent C. Dodds"/><br /><sub><b>Kent C. Dodds</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=kentcdodds" title="Documentation">📖</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=kentcdodds" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jccguimaraes"><img src="https://avatars.githubusercontent.com/u/14871650?v=3" width="100px;" alt="João Guimarães"/><br /><sub><b>João Guimarães</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jccguimaraes" title="Code">💻</a></td>
    <td align="center"><a href="http://beneb.info"><img src="https://avatars.githubusercontent.com/u/1282980?v=3" width="100px;" alt="Ben Briggs"/><br /><sub><b>Ben Briggs</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=ben-eb" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/itaisteinherz"><img src="https://avatars.githubusercontent.com/u/22768990?v=3" width="100px;" alt="Itai Steinherz"/><br /><sub><b>Itai Steinherz</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=itaisteinherz" title="Documentation">📖</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=itaisteinherz" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/alexjoverm"><img src="https://avatars.githubusercontent.com/u/5701162?v=3" width="100px;" alt="Alex Jover"/><br /><sub><b>Alex Jover</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=alexjoverm" title="Code">💻</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=alexjoverm" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://jerodsanto.net"><img src="https://avatars3.githubusercontent.com/u/8212?v=3" width="100px;" alt="Jerod Santo"/><br /><sub><b>Jerod Santo</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jerodsanto" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/kevinjalbert"><img src="https://avatars1.githubusercontent.com/u/574871?v=3" width="100px;" alt="Kevin Jalbert"/><br /><sub><b>Kevin Jalbert</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=kevinjalbert" title="Code">💻</a></td>
    <td align="center"><a href="https://i.am.charlike.online"><img src="https://avatars3.githubusercontent.com/u/5038030?v=4" width="100px;" alt="tunnckoCore"/><br /><sub><b>tunnckoCore</b></sub></a><br /><a href="#tool-charlike" title="Tools">🔧</a></td>
    <td align="center"><a href="https://machour.idk.tn/"><img src="https://avatars2.githubusercontent.com/u/304450?v=4" width="100px;" alt="Mehdi Achour"/><br /><sub><b>Mehdi Achour</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=machour" title="Code">💻</a></td>
    <td align="center"><a href="https://codsen.com"><img src="https://avatars1.githubusercontent.com/u/8344688?v=4" width="100px;" alt="Roy Revelt"/><br /><sub><b>Roy Revelt</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/issues?q=author%3Arevelt" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/chrisinajar"><img src="https://avatars1.githubusercontent.com/u/422331?v=4" width="100px;" alt="Chris Vickery"/><br /><sub><b>Chris Vickery</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=chrisinajar" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/brycereynolds"><img src="https://avatars2.githubusercontent.com/u/1026002?v=4" width="100px;" alt="Bryce Reynolds"/><br /><sub><b>Bryce Reynolds</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=brycereynolds" title="Code">💻</a></td>
    <td align="center"><a href="http://www.jmeas.com"><img src="https://avatars3.githubusercontent.com/u/2322305?v=4" width="100px;" alt="James, please"/><br /><sub><b>James, please</b></sub></a><br /><a href="#ideas-jmeas" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jmeas" title="Code">💻</a></td>
    <td align="center"><a href="http://www.spyros.io"><img src="https://avatars3.githubusercontent.com/u/1057324?v=4" width="100px;" alt="Spyros Ioakeimidis"/><br /><sub><b>Spyros Ioakeimidis</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=spirosikmd" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/fadc80"><img src="https://avatars3.githubusercontent.com/u/12335761?v=4" width="100px;" alt="Fernando Costa"/><br /><sub><b>Fernando Costa</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=fadc80" title="Code">💻</a></td>
    <td align="center"><a href="https://snipe.net"><img src="https://avatars0.githubusercontent.com/u/197404?v=4" width="100px;" alt="snipe"/><br /><sub><b>snipe</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=snipe" title="Documentation">📖</a></td>
    <td align="center"><a href="http://gantlaborde.com/"><img src="https://avatars0.githubusercontent.com/u/997157?v=4" width="100px;" alt="Gant Laborde"/><br /><sub><b>Gant Laborde</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=GantMan" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://in.linkedin.com/in/mzubairahmed"><img src="https://avatars2.githubusercontent.com/u/17708702?v=4" width="100px;" alt="Md Zubair Ahmed"/><br /><sub><b>Md Zubair Ahmed</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=M-ZubairAhmed" title="Documentation">📖</a> <a href="https://github.com/Sanji515/all-contributors-cli/issues?q=author%3AM-ZubairAhmed" title="Bug reports">🐛</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=M-ZubairAhmed" title="Code">💻</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=M-ZubairAhmed" title="Tests">⚠️</a></td>
    <td align="center"><a href="http://bogas04.github.io"><img src="https://avatars3.githubusercontent.com/u/6177621?v=4" width="100px;" alt="Divjot Singh"/><br /><sub><b>Divjot Singh</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=bogas04" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/tigermarques"><img src="https://avatars0.githubusercontent.com/u/15315098?v=4" width="100px;" alt="João Marques"/><br /><sub><b>João Marques</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=tigermarques" title="Code">💻</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=tigermarques" title="Documentation">📖</a> <a href="#ideas-tigermarques" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="http://hipstersmoothie.com"><img src="https://avatars3.githubusercontent.com/u/1192452?v=4" width="100px;" alt="Andrew Lisowski"/><br /><sub><b>Andrew Lisowski</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=hipstersmoothie" title="Code">💻</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=hipstersmoothie" title="Documentation">📖</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=hipstersmoothie" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/chinesedfan"><img src="https://avatars3.githubusercontent.com/u/1736154?v=4" width="100px;" alt="Xianming Zhong"/><br /><sub><b>Xianming Zhong</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=chinesedfan" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/xuchaoying"><img src="https://avatars2.githubusercontent.com/u/8073251?v=4" width="100px;" alt="C.Y.Xu"/><br /><sub><b>C.Y.Xu</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=xuchaoying" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/chris-dura"><img src="https://avatars3.githubusercontent.com/u/3680914?v=4" width="100px;" alt="Dura"/><br /><sub><b>Dura</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=chris-dura" title="Documentation">📖</a></td>
    <td align="center"><a href="https://jakebolam.com"><img src="https://avatars2.githubusercontent.com/u/3534236?v=4" width="100px;" alt="Jake Bolam"/><br /><sub><b>Jake Bolam</b></sub></a><br /><a href="#infra-jakebolam" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jakebolam" title="Code">💻</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jakebolam" title="Documentation">📖</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jakebolam" title="Tests">⚠️</a></td>
    <td align="center"><a href="http://maxcubing.wordpress.com"><img src="https://avatars0.githubusercontent.com/u/8260834?v=4" width="100px;" alt="Maximilian Berkmann"/><br /><sub><b>Maximilian Berkmann</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=Berkmann18" title="Code">💻</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=Berkmann18" title="Tests">⚠️</a> <a href="https://github.com/Sanji515/all-contributors-cli/commits?author=Berkmann18" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/tbenning"><img src="https://avatars2.githubusercontent.com/u/7265547?v=4" width="100px;" alt="tbenning"/><br /><sub><b>tbenning</b></sub></a><br /><a href="#design-tbenning" title="Design">🎨</a></td>
    <td align="center"><a href="https://twitter.com/ehmicky"><img src="https://avatars2.githubusercontent.com/u/8136211?v=4" width="100px;" alt="ehmicky"/><br /><sub><b>ehmicky</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=ehmicky" title="Code">💻</a></td>
    <td align="center"><a href="https://ghuser.io/jamesgeorge007"><img src="https://avatars2.githubusercontent.com/u/25279263?v=4" width="100px;" alt="James George"/><br /><sub><b>James George</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=jamesgeorge007" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/nschonni"><img src="https://avatars2.githubusercontent.com/u/1297909?v=4" width="100px;" alt="Nick Schonning"/><br /><sub><b>Nick Schonning</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=nschonni" title="Code">💻</a></td>
    <td align="center"><a href="https://cezaraugusto.net/"><img src="https://avatars0.githubusercontent.com/u/4672033?v=4" width="100px;" alt="Cezar Augusto"/><br /><sub><b>Cezar Augusto</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=cezaraugusto" title="Documentation">📖</a></td>
    <td align="center"><a href="https://reinhold.is"><img src="https://avatars1.githubusercontent.com/u/5678122?v=4" width="100px;" alt="Jeppe Reinhold"/><br /><sub><b>Jeppe Reinhold</b></sub></a><br /><a href="https://github.com/Sanji515/all-contributors-cli/commits?author=JReinhold" title="Code">💻</a></td>
    <td align="center"><a href="https://sanji515.github.io/"><img src="https://avatars1.githubusercontent.com/u/32524438?v=4" width="100px;" alt="Sanjeev Singh"/><br /><sub><b>Sanjeev Singh</b></sub></a><br /><a href="#maintenance-Sanji515" title="Maintenance">🚧</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->


## Contribution guidelines

If you are interested in contributing to EvalAI, follow our [contribution guidelines](https://github.com/Cloud-CV/EvalAI/blob/master/.github/CONTRIBUTING.md).
