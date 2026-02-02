# Caffe
**URL:** https://caffe.berkeleyvision.org
**Page Title:** Caffe | Deep Learning Framework
--------------------


## Caffe

Caffe is a deep learning framework made with expression, speed, and modularity in mind.
It is developed by Berkeley AI Research ( BAIR ) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley.
Caffe is released under the BSD 2-Clause license .
[LINK: BSD 2-Clause license](https://github.com/BVLC/caffe/blob/master/LICENSE)
Check out our web image classification demo !

## Why Caffe?

Expressive architecture encourages application and innovation.
Models and optimization are defined by configuration without hard-coding.
Switch between CPU and GPU by setting a single flag to train on a GPU machine then deploy to commodity clusters or mobile devices.
Extensible code fosters active development.
In Caffe’s first year, it has been forked by over 1,000 developers and had many significant changes contributed back.
Thanks to these contributors the framework tracks the state-of-the-art in both code and models.
Speed makes Caffe perfect for research experiments and industry deployment.
Caffe can process over 60M images per day with a single NVIDIA K40 GPU*.
That’s 1 ms/image for inference and 4 ms/image for learning and more recent library versions and hardware are faster still.
We believe that Caffe is among the fastest convnet implementations available.
Community : Caffe already powers academic research projects, startup prototypes, and even large-scale industrial applications in vision, speech, and multimedia.
Join our community of brewers on the caffe-users group and Github .
[LINK: Github](https://github.com/BVLC/caffe/)
* With the ILSVRC2012-winning SuperVision model and prefetching IO.

## Documentation

- DIY Deep Learning for Vision with Caffe and Caffe in a Day Tutorial presentation of the framework and a full-day crash course.
[LINK: DIY Deep Learning for Vision with Caffe](https://docs.google.com/presentation/d/1UeKXVgRvvxg9OUdh_UiC5G71UMscNPlvArsWER41PsU/edit#slide=id.p)
[LINK: Caffe in a Day](https://docs.google.com/presentation/d/1HxGdeq8MPktHaPb-rlmYYQ723iWzq9ur6Gjo71YiG0Y/edit#slide=id.gc2fcdcce7_216_0)
- Tutorial Documentation Practical guide and framework reference.
- arXiv / ACM MM ‘14 paper A 4-page report for the ACM Multimedia Open Source competition (arXiv:1408.5093v1).
- Installation instructions Tested on Ubuntu, Red Hat, OS X.
- Model Zoo BAIR suggests a standard distribution format for Caffe models, and provides trained models.
- Developing & Contributing Guidelines for development and contributing to Caffe.
- API Documentation Developer documentation automagically generated from code comments.
- Benchmarking Comparison of inference and learning for different networks and GPUs.
[LINK: Benchmarking](https://docs.google.com/spreadsheets/d/1Yp4rqHpT7mKxOPbpzYeUfEFLnELDAgxSSBQKp5uKDGQ/edit#gid=0)

### Notebook Examples

- Image Classification and Filter Visualization Instant recognition with a pre-trained model and a tour of the net interface for visualizing features and parameters layer-by-layer.
[LINK: Image Classification and Filter Visualization](http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/00-classification.ipynb)
- Learning LeNet Define, train, and test the classic LeNet with the Python interface.
[LINK: Learning LeNet](http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/01-learning-lenet.ipynb)
- Fine-tuning for Style Recognition Fine-tune the ImageNet-trained CaffeNet on new data.
[LINK: Fine-tuning for Style Recognition](http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/02-fine-tuning.ipynb)
- Off-the-shelf SGD for classification Use Caffe as a generic SGD optimizer to train logistic regression on non-image HDF5 data.
[LINK: Off-the-shelf SGD for classification](http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/brewing-logreg.ipynb)
- Multilabel Classification with Python Data Layer Multilabel classification on PASCAL VOC using a Python data layer.
[LINK: Multilabel Classification with Python Data Layer](http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/pascal-multilabel-with-datalayer.ipynb)
- Editing model parameters How to do net surgery and manually change model parameters for custom use.
[LINK: Editing model parameters](http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/net_surgery.ipynb)
- R-CNN detection Run a pretrained model as a detector in Python.
[LINK: R-CNN detection](http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/detection.ipynb)
- Siamese network embedding Extracting features and plotting the Siamese network embedding.
[LINK: Siamese network embedding](http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/siamese/mnist_siamese.ipynb)

### Command Line Examples

- ImageNet tutorial Train and test "CaffeNet" on ImageNet data.
- LeNet MNIST Tutorial Train and test "LeNet" on the MNIST handwritten digit data.
- CIFAR-10 tutorial Train and test Caffe on CIFAR-10 data.
- Fine-tuning for style recognition Fine-tune the ImageNet-trained CaffeNet on the "Flickr Style" dataset.
- Feature extraction with Caffe C++ code. Extract CaffeNet / AlexNet features using the Caffe utility.
- CaffeNet C++ Classification example A simple example performing image classification using the low-level C++ API.
- Web demo Image classification demo running as a Flask web server.
- Siamese Network Tutorial Train and test a siamese network on MNIST data.

## Citing Caffe

Please cite Caffe in your publications if it helps your research:
If you do publish a paper where Caffe helped your research, we encourage you to cite the framework for tracking by Google Scholar .

## Contacting Us

Join the caffe-users group to ask questions and discuss methods and models. This is where we talk about usage, installation, and applications.
Framework development discussions and thorough bug reports are collected on Issues .
[LINK: Issues](https://github.com/BVLC/caffe/issues)

## Acknowledgements

The BAIR Caffe developers would like to thank NVIDIA for GPU donation, A9 and Amazon Web Services for a research grant in support of Caffe development and reproducible research in deep learning, and BAIR PI Trevor Darrell for guidance.
The BAIR members who have contributed to Caffe are (alphabetical by first name): Carl Doersch , Eric Tzeng , Evan Shelhamer , Jeff Donahue , Jon Long , Philipp Krähenbühl , Ronghang Hu , Ross Girshick , Sergey Karayev , Sergio Guadarrama , Takuya Narihira , and Yangqing Jia .
[LINK: Eric Tzeng](https://github.com/erictzeng)
[LINK: Jon Long](https://github.com/longjon)
[LINK: Takuya Narihira](https://github.com/tnarihi)
The open-source community plays an important and growing role in Caffe’s development.
Check out the Github project pulse for recent activity and the contributors for the full list.
[LINK: project pulse](https://github.com/BVLC/caffe/pulse)
[LINK: contributors](https://github.com/BVLC/caffe/graphs/contributors)
We sincerely appreciate your interest and contributions!
If you’d like to contribute, please read the developing & contributing guide.
Yangqing would like to give a personal thanks to the NVIDIA Academic program for providing GPUs, Oriol Vinyals for discussions along the journey, and BAIR PI Trevor Darrell for advice.

--------------------