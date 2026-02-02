# Doubao 1.5 Pro
**URL:** https://team.doubao.com/en/special/doubao_1_5_pro
**Page Title:** Doubao 1.5pro - Doubao Team
--------------------

- 表格中，其它模型的评测指标来自官方评测结果，官方评测结果中不含的部分来自内部评测平台结果
- GPT4o-0806 在语言模型公开评测指标中显著优于 GPT4o 其它版本，详见：https://github.com/openai/simple-evals
- Doubao-Dense 和 Doubao-MoE 均为 9T tokens 的数据的阶段性结果，数据分布完全相同；MoE 模型的性能略优于整体参数量为 MoE 激活参数量 7 倍的稠密模。
- Llama3.1-405B 为 15T tokens 的最终结果，数据分布和 Doubao 模型不同，Doubao 稠密模型的参数量也远小于 Llama3.1-405B，从结果上可以看到 Doubao 预训练的数据质量和训练超参更优；MoE 模型完整训练后的性能比 9T tokens 数据的中间版本有更大提升。
- Prefill Attention: 使用 MMA/WGMMA 等指令扩展开源的 FlashAttention 8-bit 实现，结合 Per N tokens Per Sequence 的量化策略，确保该阶段可以在不同架构的 GPU 上无损运行。同时，通过建模不同长度分片的 Attention 耗时，并结合动态跨 Query Batching 的策略，实现 Chunk-PP Serving 时的卡间均衡，有效消除负载不均衡引起的空跑；
- Prefill FFN: 采用 W4A8 量化，有效降低了稀疏 MoE 专家的访存开销，并通过跨 Query Batching 的策略，给到FFN阶段更多输入，使 MFU 提升至 0.8.
- Decode Attention： 采用 TP 方式部署，并通过启发式搜索以及激进的长句拆分策略，优化单 batch 内不同 Query KV 长度差异大的常见场景；精度上，依然采用 Per N tokens Per Sequence 量化方式；此外，还优化了随机采样过程中的 Attention 计算，保证 KV Cache 只被访问一次。
- Decode FFN： 保持 W4A8 量化，采用 EP 方式部署。
- 针对 Tensor 传输进行定制化的 RPC Backend，并通过零拷贝、多流并行等手段优化了 TCP/RDMA 网络上的 Tensor 传输效率，进而提升 PD 分离下的 KV Cache 传输效率。
- 支持 Prefill 跟 Decode 集群的灵活配比和动态扩缩，对每种角色独立做 HPA 弹性扩容，保障 Prefill 和 Decode 都无冗余算力，两边算力配比贴合线上实际流量模式。
- 在框架上将 GPU 计算和 CPU 前后处理异步化，使得 GPU 推理第 N 步时 CPU 提前发射第 N+1 步 Kernel，保持 GPU 始终被打满，整个框架处理动作对 GPU 推理零开销。
- 评测中 GPT4o-1120 在多模态能力上优于 GPT4o-0806。

--------------------