from transformers import pipeline

summarizer = pipeline(
    "summarization", model="knkarthick/bart-large-xsum-samsum")

conversation_1 = ''''Amiya Panigrahi: Try get the one there.',
  'Megan Bowen: Uh-huh.',
  'Amiya Panigrahi: When I try hello.',
  'Amiya Panigrahi: Master everyday example bro.',
  'Amiya Panigrahi: Hello, good morning.',
  "Megan Bowen: Hi I'm a goodnight.",
  "Amiya Panigrahi: I'm running 10 minutes late. Could you guys just late? Mary know that I'm.",
  "Amiya Panigrahi: I'm coming and I'll present today before she starts.",
  "Megan Bowen: Sure, no problem. I'll save a seat for you.",
  'Amiya Panigrahi: Thank you, Megan.',
  'Amiya Panigrahi: Megan, can you please do the equity task on priority?',
  "Megan Bowen: I'm already occupied with the Canada Task. Can you ask Larry to do this?",
  'Amiya Panigrahi: OK, see you. Thank you for saying this.',
  'Megan Bowen: OK. Thank you, Amiya.',
  'Amiya Panigrahi: Thank you. Bye.',
  'Megan Bowen: Bye.'                                     
'''

print(summarizer(conversation_1))
