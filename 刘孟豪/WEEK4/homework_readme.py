# #week3作业
#
# #词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改

#
# #待切分文本
# sentence = "经常有意见分歧"
#
# #实现全切分函数，输出根据字典能够切分出的所有的切分方式
# def all_cut(sentence, Dict):
#     #TODO
#     return target
#
# #目标输出;顺序不重要
# target = [
#     ['经常', '有意见', '分歧'],
#     ['经常', '有意见', '分', '歧'],
#     ['经常', '有', '意见', '分歧'],
#     ['经常', '有', '意见', '分', '歧'],
#     ['经常', '有', '意', '见分歧'],
#     ['经常', '有', '意', '见', '分歧'],
#     ['经常', '有', '意', '见', '分', '歧'],
#     ['经', '常', '有意见', '分歧'],
#     ['经', '常', '有意见', '分', '歧'],
#     ['经', '常', '有', '意见', '分歧'],
#     ['经', '常', '有', '意见', '分', '歧'],
#     ['经', '常', '有', '意', '见分歧'],
#     ['经', '常', '有', '意', '见', '分歧'],
#     ['经', '常', '有', '意', '见', '分', '歧']
# ]

sentence = '经常有意见分歧'
Dict = {"经常": 0.1,
        "经": 0.05,
        "有": 0.1,
        "常": 0.001,
        "有意见": 0.1,
        "歧": 0.001,
        "意见": 0.2,
        "分歧": 0.2,
        "见": 0.05,
        "意": 0.05,
        "见分歧": 0.05,
        "分": 0.1}
def get_whole_juzi(start):
    if start == len(sentence):  #7
        return [[]]  # 句子完整，递归结束
    results = []
    for i in range(start, len(sentence) + 1):
        print(i)
        word = sentence[start:i]
        if word in Dict:  # 如果当前词在词典中
            for res in get_whole_juzi(i):
                # 补齐
                results.append([word] + res)
    return results
res = get_whole_juzi(0)
print(len(res))
print(res)
