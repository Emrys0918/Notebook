data_path = "the-verdict.txt"
with open (data_path,"r",encoding = "utf-8") as f:
    data = f.read()
print(f"总字符数为: {len(data)}")
print(f"前100个字符:{data[:100]}")