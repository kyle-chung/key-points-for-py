在字典遍历过程中修改字典元素，报错 RuntimeError: dictionary changed size during iteration

得知遍历时不能修改字典元素

for k in func_dict.keys():
    if func_dict[k] is np.nan:
        del func_dict[k]
        continue
        
解决办法：将遍历条件改为列表

for k in list(func_dict.keys()):
    if func_dict[k] is np.nan:
        del func_dict[k]
        continue
