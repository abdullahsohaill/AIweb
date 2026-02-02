# CPU® 2017 Benchmark Suite
**URL:** https://webdocs.cs.ualberta.ca/~amaral/AlbertaWorkloadsForSPECCPU2017
**Page Title:** The Alberta Workloads for the SPEC CPU<sup>®</sup> 2017 Benchmark Suite
--------------------


## The Alberta Workloads for the SPEC CPU ® 2017 Benchmark Suite

- All Benchmarks
- Workloads List
- Scripts List
- Reports List
This is a collection of additional workloads for the SPEC CPU2017 Benchmark Suite. These workloads were collected by a research group at the University of Alberta led by Prof. J. Nelson Amaral with collaboration from Edson Borin's group at the Universidade de Campinas in Brazil.
This site contains both additional workloads for the benchmarks included in the suite and, for some benchmarks, scripts that can be used to generate additional workloads. Some of these scripts use random processes to generate inputs and thus can be used to generate a large number of new workloads. Other scripts are simply combining files from repositories or creating variations in queries used by the benchmark programs. Therefore in those cases there is a limited number of new inputs that can be generated.
The intent of these new workloads is to enable a more complete evaluation of techniques that depend on information gathered during previous executions of the same program such as compilation that use feedback directed optimization and architectural proposals that use automated learning. These additional workloads are not intended to be used for performance measurements that would be subsequently used to compare computing platforms for the sake of commercial or advertising claims. These additional workloads also cannot be used to produce performance results that are submitted for official publication in the SPEC website. For that you must follow the rules published by the SPEC Open Systems Group.
To assist researchers with the selection of inputs for their experiments, an initial evaluation of the effect of the change in inputs on the behaviour of the benchmark programs is also included in this website. While incomplete, this initial performance study can be used to determine, for instance, which program behaviours are more sensitive to changes in the program inputs.
A likely user of these workloads will be setting up an experimental environment that is different than the one use by runcpu to generate standarized results. Such a user should still be familiar with several aspects of the process for building and running a benchmark. The SPEC CPU 2017 suite distribution includes the Avoiding runcpu documentation that shall be relevant for such user.
[LINK: Avoiding runcpu](https://www.spec.org/cpu2017/Docs/runcpu-avoidance.html)
The following article provides an overview of the Alberta Workloads for teh SPEC CPU 2017 Benchmark Suite, including a summary of the process to obtain new workloads for the various benchmarks:
José Nelson Amaral, Edson Borin, Dylan R. Ashley, Caian Benedicto, Elliot Colp, João Henrique Stange Hoffmam, Marcus Karpoff, Erick Ochoa, Morgan Redshaw, Raphael Ernani Rodrigues, " The Alberta Workloads for the SPEC CPU 2017 Benchmark Suite ," International Symposium on Performance Analysis of Systems and Software , Belfast, Northern Ireland, April, 2018.
Most workloads include new inputs as well as expected outputs. Work has been done to reduce difficulty in integrating these new workloads into SPEC CPU2017. The new workloads follow the same directory structure as the reference workloads. When possible, the inputs and outputs follow the same naming convention as SPEC's reference workloads to take advantage of output validation. The outputs provided are the ones that were obtained in the research laboratories at the University of Alberta when the benchmark was running with the corresponding inputs. No claims are made as to the correctness of such output. If you discover that a given output is incorrect, please contact J. Nelson Amaral.

--------------------