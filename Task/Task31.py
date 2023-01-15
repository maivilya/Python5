text = "дядя ваня ехал на метро, он ехал не быстро: примерно 50 к в час. с ним в машине была его собака жучка."

while "," in text or ":" in text or "." in text:
    text = text.replace(",", "")
    text = text.replace(":", "")
    text = text.replace(".", "")
    break

text_list = text.split()
print(text_list)

count = 0
while count < len(text_list):
    for word in text_list:
        if "а" in word or "б" in word or "в" in word:
            text_list.remove(word)
    count+=1

print("result -> ",text_list)