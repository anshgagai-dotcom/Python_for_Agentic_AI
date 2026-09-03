import time

HISTOSRY_OF_INDIA = """ 
🇮🇳 History of India — Complete Overview

Indian history is one of the oldest and most diverse histories in the world, spanning thousands of years. A simple way to understand it is to divide it into major periods:

1. 🏺 Ancient India
c. 3300 BCE  700 CE
Indus Valley Civilization — Harappa, Mohenjo-daro, Dholavira
Vedic Period — Vedas, early kingdoms, development of Sanskrit traditions
Mahajanapadas — rise of large states such as Magadha
Buddhism & Jainism — Gautama Buddha and Mahavira
Mauryan Empire — Chandragupta Maurya and Ashoka
Gupta Empire — major developments in mathematics, astronomy, literature and arts
Later ancient kingdoms and regional powers

2. 🏰 Medieval India
c. 700  1750 CE
Regional kingdoms such as the Cholas, Pallavas, Rashtrakutas, Rajputs and Pala Empire
Delhi Sultanate
Mamluk/Slave dynasty
Khalji dynasty
Tughlaq dynasty
Sayyid dynasty
Lodi dynasty
Vijayanagara Empire
Bhakti and Sufi movements
Mughal Empire
Babur
Humayun
Akbar
Jahangir
Shah Jahan
Aurangzeb
Rise of the Marathas, including Chhatrapati Shivaji Maharaj
Decline of Mughal political power

3. 🇬🇧 British / Colonial India
c. 1757  1947
Expansion of the British East India Company
Battle of Plassey (1757)
British territorial expansion
Economic and administrative changes
Revolt of 1857
Crown rule beginning in 1858
Formation of the Indian National Congress (1885)
Growth of the independence movement
Mahatma Gandhi and mass movements:
Non-Cooperation Movement
Civil Disobedience Movement
Quit India Movement
Revolutionary movements and other streams of nationalism
World Wars and their impact on India
Indian independence in 1947
Partition and creation of India and Pakistan

4. 🇮🇳 Independent India
1947  Present
Independence and Partition
Constitution adopted in 1950
India becomes a republic
First general elections in 1951 52
Economic planning and industrial development
Wars and major geopolitical events
Green Revolution
Economic liberalization in 1991
Growth of IT, services and technology
Digital transformation
India as a major global economic and geopolitical power
 """


def stream_responce(text):
    for word in text.split():
        time.sleep(0.1)
        yield word

gen_streamer = stream_responce(HISTOSRY_OF_INDIA)
for word in gen_streamer:
    print(word, end = " ", flush = True)



