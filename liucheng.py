# 定义一个列表存储三个流程
processes = ['Process1', 'Process2', 'Process3']

# 循环遍历每个流程
for process in processes:
    print(f'Starting {process}')
    
    # 模拟执行流程
    for i in range(1, 6):
        print(f'{process} step {i}')
    
    print(f'{process} completed\n')
