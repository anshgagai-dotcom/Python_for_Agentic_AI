"""
Project 15 — Safe Shopping Cart (mutable-default trap)
EN: Write add_item(item, cart=None) correctly so that each fresh call (without a cart) starts with an EMPTY cart. Call it 3 separate times and show each returns only its own item. (Do NOT use cart=[] — explain in a comment why.)
हिंदी: add_item(item, cart=None) सही तरीके से बनाओ ताकि हर नई call (बिना cart के) खाली cart से शुरू हो। इसे 3 अलग बार call करके दिखाओ कि हर बार सिर्फ़ अपना item आता है। (cart=[] मत इस्तेमाल करो — comment में कारण लिखो।)
Concepts: mutable default trap, None sentinel, is None
Hint: if cart is None: cart = [] — this makes a fresh list every call.
"""

