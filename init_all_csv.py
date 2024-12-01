import pandas
with open('output_data.csv', 'w') as f:
    f.write('bus,Real,imag,p,q\n')  # 写入表头
with open('inp_train_2244.csv', 'w') as file:
    pass  # 什么也不写，文件内容就被清空了
with open('otp_train_66.csv', 'w') as file:
    pass  # 什么也不写，文件内容就被清空了
with open('out_test_data.csv', 'w') as f:
    f.write('bus,Real,imag,p,q\n')  # 写入表头
with open('inp_test_2244.csv', 'w') as file:
    pass  # 什么也不写，文件内容就被清空了
with open('otp_test_66.csv', 'w') as file:
    pass  # 什么也不写，文件内容就被清空了