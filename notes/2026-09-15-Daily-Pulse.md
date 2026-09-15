# Daily Pulse - 2026-09-15

### [blknoiz06](https://twitter.com/blknoiz06/status/2099555851082051764)

**发布时间:** 2026-09-14 17:48:17 | ❤️ 3491

> big week

> 🇨🇳 译文：big week

[🔗 查看原帖](https://twitter.com/blknoiz06/status/2099555851082051764)

---

### [NoLimitGains](https://twitter.com/NoLimitGains/status/2099404915860787347)

**发布时间:** 2026-09-14 07:48:31 | ❤️ 4761

> In 1998, Warren Buffett gave a free hour-long talk on how to NEVER lose money in the market.

Watch it today, no matter what. https://t.co/7meXr0fmx7

> 🇨🇳 译文：In 1998, Warren Buffett gave a free hour-long talk on how to NEVER lose money in the market.

Watch it today, no matter what. https://t.co/7meXr0fmx7

[🔗 查看原帖](https://twitter.com/NoLimitGains/status/2099404915860787347)

---

### [mcuban](https://twitter.com/mcuban/status/2099552895083430085)

**发布时间:** 2026-09-14 17:36:32 | ❤️ 5459

> Hey @grok , which  is more likely to create a human extinction event or series of events in the next 25 years , AI or Climate Change ? Assign a probability  to each

If the answer to either is yes, do your best to put a timeline for when you think  it happens 

If the answer is no. Explain why

> 🇨🇳 译文：Hey @grok , which  is more likely to create a human extinction event or series of events in the next 25 years , AI or Climate Change ? Assign a probability  to each

If the answer to either is yes, do your best to put a timeline for when you think  it happens 

If the answer is no. Explain why

[🔗 查看原帖](https://twitter.com/mcuban/status/2099552895083430085)

---

### [KobeissiLetter](https://twitter.com/KobeissiLetter/status/2099542528294793269)

**发布时间:** 2026-09-14 16:55:21 | ❤️ 3833

> BREAKING: The Dow Jones Industrial Average erases all losses and turns green on the day after President Trump says Iran wants to make a peace deal. https://t.co/5y90YVeDHe

> 🇨🇳 译文：BREAKING: The Dow Jones Industrial Average erases all losses and turns green on the day after President Trump says Iran wants to make a peace deal. https://t.co/5y90YVeDHe

![Image](images/img_82c12566-988e-44db-b925-f4153fcfe18e.jpg)

[🔗 查看原帖](https://twitter.com/KobeissiLetter/status/2099542528294793269)

---

### [addyosmani](https://twitter.com/addyosmani/status/2099577600159158765)

**发布时间:** 2026-09-14 19:14:42 | ❤️ 2480

> At Anthropic, Claude now writes 80% of our code. Engineers ship 8x more code per quarter. 

Side effect: Tests grew 10x. CI jobs up 25x in 6 months. Here's what helped us scale:

https://t.co/WOL2r60vAE https://t.co/7vf60noTQt

> 🇨🇳 译文：At Anthropic, Claude now writes 80% of our code. Engineers ship 8x more code per quarter. 

Side effect: Tests grew 10x. CI jobs up 25x in 6 months. Here's what helped us scale:

https://t.co/WOL2r60vAE https://t.co/7vf60noTQt

![Image](images/img_cd0a2d0d-8333-43a9-9287-2e15093ace2e.jpg)

[🔗 查看原帖](https://twitter.com/addyosmani/status/2099577600159158765)

---

### [SakanaAILabs](https://twitter.com/SakanaAILabs/status/2099468208231399687)

**发布时间:** 2026-09-14 12:00:01 | ❤️ 1896

> Introducing PC-ALM, a local-learning alternative to backpropagation.

Our method trains 1000-layer neural nets using only local dynamics, and without backprop.

Blog: https://t.co/bBGCgalqKW

Standard deep learning relies on backpropagation. The brain, however, cannot implement backpropagation, at least not exactly. How can a physical system, such as the brain, solve multilayer credit assignment without explicit use of backprop?

We look for inspiration in two related fields: distributed optimization and NeuroAI.

In NeuroAI, predictive coding asks each neuron activation to solve an energy-based inference problem instead of using a standard forward pass. That inference step can be implemented as energy-minimization dynamics on local prediction errors.

This perspective -- each layer as a dynamical system -- has proven promising, but performance of predictive coding hasn't scaled well with depth. Credit signals at far ends of the network struggle to diffuse into internal layers.

We turn to distributed optimization, generalizing predictive coding to use an augmented Lagrangian instead of energy. This motivation stems back to a classic 1988 paper by LeCun, showing that the Lagrange multipliers of a deep network can be identified with gradients of a supervised loss. The augmented Lagrangian then bridges LeCun's perspective to the standard predictive coding that is used in NeuroAI.

We find that this new perspective yields a natural PC-like alternative to backpropagation, resulting in a method we call PC-ALM. PC-ALM differs from PC in that it introduces dual neurons (Lagrange multipliers) as part of the layer-local dynamics, resulting in each layer acting as a PI feedback control system to minimize local prediction errors.

We find that PC-ALM is capable of propagating signals to seemingly arbitrary depth, especially in deep narrow networks where standard PC struggles to learn.

Ultimately, our motivation here is to understand how distributed physical systems, such as the brain, can compute credit signals using only local coupling and local dynamics.

PC-ALM may also inform deep learning in neuromorphic hardware, where dynamics are cheaper than on GPUs.

Paper: https://t.co/doSZ8mzoyK
Code: https://t.co/rxEDIszVKD

> 🇨🇳 译文：Introducing PC-ALM, a local-learning alternative to backpropagation.

Our method trains 1000-layer neural nets using only local dynamics, and without backprop.

Blog: https://t.co/bBGCgalqKW

Standard deep learning relies on backpropagation. The brain, however, cannot implement backpropagation, at least not exactly. How can a physical system, such as the brain, solve multilayer credit assignment without explicit use of backprop?

We look for inspiration in two related fields: distributed optimization and NeuroAI.

In NeuroAI, predictive coding asks each neuron activation to solve an energy-based inference problem instead of using a standard forward pass. That inference step can be implemented as energy-minimization dynamics on local prediction errors.

This perspective -- each layer as a dynamical system -- has proven promising, but performance of predictive coding hasn't scaled well with depth. Credit signals at far ends of the network struggle to diffuse into internal layers.

We turn to distributed optimization, generalizing predictive coding to use an augmented Lagrangian instead of energy. This motivation stems back to a classic 1988 paper by LeCun, showing that the Lagrange multipliers of a deep network can be identified with gradients of a supervised loss. The augmented Lagrangian then bridges LeCun's perspective to the standard predictive coding that is used in NeuroAI.

We find that this new perspective yields a natural PC-like alternative to backpropagation, resulting in a method we call PC-ALM. PC-ALM differs from PC in that it introduces dual neurons (Lagrange multipliers) as part of the layer-local dynamics, resulting in each layer acting as a PI feedback control system to minimize local prediction errors.

We find that PC-ALM is capable of propagating signals to seemingly arbitrary depth, especially in deep narrow networks where standard PC struggles to learn.

Ultimately, our motivation here is to understand how distributed physical systems, such as the brain, can compute credit signals using only local coupling and local dynamics.

PC-ALM may also inform deep learning in neuromorphic hardware, where dynamics are cheaper than on GPUs.

Paper: https://t.co/doSZ8mzoyK
Code: https://t.co/rxEDIszVKD

[🔗 查看原帖](https://twitter.com/SakanaAILabs/status/2099468208231399687)

---

### [CEOAdam](https://twitter.com/CEOAdam/status/2099671187903144399)

**发布时间:** 2026-09-15 01:26:35 | ❤️ 898

> In my crosshairs as much as Robinhood’s shameful Stock Tokens and the trademark- infringing meme coins that they trade: dreaded TICKET SCALPERS. 

So far, we have reclaimed more than 1,600 AMC tickets from resale sites posted there. 

Scalpers beware, AMC is coming after you. https://t.co/UrrX0EYhoc

> 🇨🇳 译文：In my crosshairs as much as Robinhood’s shameful Stock Tokens and the trademark- infringing meme coins that they trade: dreaded TICKET SCALPERS. 

So far, we have reclaimed more than 1,600 AMC tickets from resale sites posted there. 

Scalpers beware, AMC is coming after you. https://t.co/UrrX0EYhoc

![Image](images/img_7ccc3897-3cd0-45db-bc16-075e882d9f56.jpg)

[🔗 查看原帖](https://twitter.com/CEOAdam/status/2099671187903144399)

---

### [MTSlive](https://twitter.com/MTSlive/status/2099537693080428904)

**发布时间:** 2026-09-14 16:36:08 | ❤️ 3506

> SITUATION DETECTED: Nvidia, Palantir, and Booz Allen Hamilton are restricting or eliminating the use of Anthropic and OpenAI models in some cases due to rising corporate data retention and intellectual property concerns, per The Information.

> 🇨🇳 译文：SITUATION DETECTED: Nvidia, Palantir, and Booz Allen Hamilton are restricting or eliminating the use of Anthropic and OpenAI models in some cases due to rising corporate data retention and intellectual property concerns, per The Information.

[🔗 查看原帖](https://twitter.com/MTSlive/status/2099537693080428904)

---

### [DoWCTO](https://twitter.com/DoWCTO/status/2099536442594582922)

**发布时间:** 2026-09-14 16:31:10 | ❤️ 6280

> Americanism, not effective altruism.

The United States will continue to be AI DOMINANT! 🇺🇸 https://t.co/CQDt5s72Jl

> 🇨🇳 译文：Americanism, not effective altruism.

The United States will continue to be AI DOMINANT! 🇺🇸 https://t.co/CQDt5s72Jl

![Image](images/img_14075bbf-58f2-423c-8b18-4747b58436bf.jpg)

[🔗 查看原帖](https://twitter.com/DoWCTO/status/2099536442594582922)

---

### [CBSNews](https://twitter.com/CBSNews/status/2099623027608633410)

**发布时间:** 2026-09-14 22:15:13 | ❤️ 2448

> EXCLUSIVE: Trump AI advisor David Sacks tells CBS News' @JoLingKent that tech leaders like Anthropic CEO and co-founder Dario Amodei have a responsibility to ensure their products are safe — and should "step aside" if they can't control what they're building. https://t.co/mDq88h7pCA

> 🇨🇳 译文：EXCLUSIVE: Trump AI advisor David Sacks tells CBS News' @JoLingKent that tech leaders like Anthropic CEO and co-founder Dario Amodei have a responsibility to ensure their products are safe — and should "step aside" if they can't control what they're building. https://t.co/mDq88h7pCA

[🔗 查看原帖](https://twitter.com/CBSNews/status/2099623027608633410)

---

### [SawyerMerritt](https://twitter.com/SawyerMerritt/status/2099665159316803948)

**发布时间:** 2026-09-15 01:02:38 | ❤️ 1479

> Elon in new All-In Summit interview on the upcoming @Tesla Roadster event on October 1st:

"We actually need an audience there to vouch that this is not AI." https://t.co/J060I5JM6Z

> 🇨🇳 译文：Elon in new All-In Summit interview on the upcoming @Tesla Roadster event on October 1st:

"We actually need an audience there to vouch that this is not AI." https://t.co/J060I5JM6Z

![Image](images/img_649ca15a-27e9-4d85-8f35-fb8668d4d968.jpg)

[🔗 查看原帖](https://twitter.com/SawyerMerritt/status/2099665159316803948)

---

### [theallinpod](https://twitter.com/theallinpod/status/2099621431621607829)

**发布时间:** 2026-09-14 22:08:53 | ❤️ 8060

> MUST SEE: Amazing moment as President Trump calls Nvidia CEO Jensen Huang while he's on stage at the All-In Summit.

@POTUS on AI Doomerism: “I'm telling you, it's all a hoax… and we're not going to let that happen.” https://t.co/ZP8cCaSMqG

> 🇨🇳 译文：MUST SEE: Amazing moment as President Trump calls Nvidia CEO Jensen Huang while he's on stage at the All-In Summit.

@POTUS on AI Doomerism: “I'm telling you, it's all a hoax… and we're not going to let that happen.” https://t.co/ZP8cCaSMqG

[🔗 查看原帖](https://twitter.com/theallinpod/status/2099621431621607829)

---

### [mirandadevine](https://twitter.com/mirandadevine/status/2099668907711660098)

**发布时间:** 2026-09-15 01:17:32 | ❤️ 732

> She's not really acquainted with any form of intelligence.

> 🇨🇳 译文：She's not really acquainted with any form of intelligence.

[🔗 查看原帖](https://twitter.com/mirandadevine/status/2099668907711660098)

---

### [BeytorunUmut](https://twitter.com/BeytorunUmut/status/2099572478049706096)

**发布时间:** 2026-09-14 18:54:21 | ❤️ 3575

> Gün sonu getiri tablosu https://t.co/V5ZUuHw2YZ

> 🇨🇳 译文：Gün sonu getiri tablosu https://t.co/V5ZUuHw2YZ

![Image](images/img_8702b8f5-124d-4d61-a1a5-748131f1c583.jpg)

[🔗 查看原帖](https://twitter.com/BeytorunUmut/status/2099572478049706096)

---

### [sama](https://twitter.com/sama/status/2099352016988614852)

**发布时间:** 2026-09-14 04:18:19 | ❤️ 19720

> There are two ways AI progress could go very badly and that we must avoid.

First, we could lose control of the future to AI. This is unacceptable; we are unapologetically on Team Humanity, and AI must always serve people. To ensure that, we need ways to ensure that alignment and safety techniques stay ahead of progress in model capabilities.

Second, we could end up in a world with too much concentration of power. If an extraordinarily powerful AI is used by one person or company to impress their worldview onto everyone else, the results could be extremely dystopian.

Avoiding these two threats requires walking a narrow middle path; for example, one country could gain too much power. Another example is one lab ending up with too much power.

> 🇨🇳 译文：There are two ways AI progress could go very badly and that we must avoid.

First, we could lose control of the future to AI. This is unacceptable; we are unapologetically on Team Humanity, and AI must always serve people. To ensure that, we need ways to ensure that alignment and safety techniques stay ahead of progress in model capabilities.

Second, we could end up in a world with too much concentration of power. If an extraordinarily powerful AI is used by one person or company to impress their worldview onto everyone else, the results could be extremely dystopian.

Avoiding these two threats requires walking a narrow middle path; for example, one country could gain too much power. Another example is one lab ending up with too much power.

[🔗 查看原帖](https://twitter.com/sama/status/2099352016988614852)

---

### [MuratMuratoglux](https://twitter.com/MuratMuratoglux/status/2099459407981449332)

**发布时间:** 2026-09-14 11:25:03 | ❤️ 6663

> Apple: 4,9 trilyon dolar. 🍏

🇹🇷Türkiye’nin “rekor” milli geliri: 1,706 trilyon dolar.
Tek şirket, yaklaşık 3 Türkiye ediyor.

Apple’ın TL değeri 237 trilyon. 
Borsa İstanbul’un tamamı 20,3 trilyon.
Bir Apple, 12 Borsa İstanbul!

Ondan sonra “Büyük Türkiye”…

> 🇨🇳 译文：Apple: 4,9 trilyon dolar. 🍏

🇹🇷Türkiye’nin “rekor” milli geliri: 1,706 trilyon dolar.
Tek şirket, yaklaşık 3 Türkiye ediyor.

Apple’ın TL değeri 237 trilyon. 
Borsa İstanbul’un tamamı 20,3 trilyon.
Bir Apple, 12 Borsa İstanbul!

Ondan sonra “Büyük Türkiye”…

[🔗 查看原帖](https://twitter.com/MuratMuratoglux/status/2099459407981449332)

---

### [NextLvlFunded](https://twitter.com/NextLvlFunded/status/2099439853012213835)

**发布时间:** 2026-09-14 10:07:21 | ❤️ 1328

> 10 x $100K Instant Funded account giveaway! 🎁  

How to Enter:  

1. Follow @NextLvlFunded &amp; @SpencerNLF 🔔 
2. Like + Retweet this and quoted post 
3. Comment to this and quoted post  

10 winners picked in 72hrs https://t.co/28YOxG0BnG

> 🇨🇳 译文：10 x $100K Instant Funded account giveaway! 🎁  

How to Enter:  

1. Follow @NextLvlFunded &amp; @SpencerNLF 🔔 
2. Like + Retweet this and quoted post 
3. Comment to this and quoted post  

10 winners picked in 72hrs https://t.co/28YOxG0BnG

![Image](images/img_e2f3a007-ed8c-44c0-be6f-dce56b11b47d.jpg)

[🔗 查看原帖](https://twitter.com/NextLvlFunded/status/2099439853012213835)

---

### [jack](https://twitter.com/jack/status/2099649359017046048)

**发布时间:** 2026-09-14 23:59:51 | ❤️ 3154

> https://t.co/qAUP2dNJsi

> 🇨🇳 译文：https://t.co/qAUP2dNJsi

[🔗 查看原帖](https://twitter.com/jack/status/2099649359017046048)

---

### [sethharpesq](https://twitter.com/sethharpesq/status/2099528407683944577)

**发布时间:** 2026-09-14 15:59:14 | ❤️ 708

> Quantum computing. Genetic engineering. Cryptocurrency. The internet of things. 3D printing. VR. Nanotechnology. Self-driving cars. Space travel. Artificial intelligence. Not one of these spurious innovations will ever live up to its hype. Not one will ever prove transformative.

> 🇨🇳 译文：Quantum computing. Genetic engineering. Cryptocurrency. The internet of things. 3D printing. VR. Nanotechnology. Self-driving cars. Space travel. Artificial intelligence. Not one of these spurious innovations will ever live up to its hype. Not one will ever prove transformative.

[🔗 查看原帖](https://twitter.com/sethharpesq/status/2099528407683944577)

---

### [bcherny](https://twitter.com/bcherny/status/2099551291601248485)

**发布时间:** 2026-09-14 17:30:10 | ❤️ 1854

> Claude Mods are landing now. Someone already built a Tetris-in-Claude mod 🤯

See issue for the latest community update, technical details, and more cool demos

https://t.co/A15qGUZ6nx https://t.co/EbE2s7FZqK

> 🇨🇳 译文：Claude Mods are landing now. Someone already built a Tetris-in-Claude mod 🤯

See issue for the latest community update, technical details, and more cool demos

https://t.co/A15qGUZ6nx https://t.co/EbE2s7FZqK

[🔗 查看原帖](https://twitter.com/bcherny/status/2099551291601248485)

