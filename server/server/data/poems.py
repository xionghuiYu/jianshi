#!/usr/bin/env python
# -*- coding: utf-8 -*-

poems = [
    '不乱于心,不困于情-不畏将来,不念过去-二零一七',
    '走了那么远- -我们去寻找一盏灯',
    '我的诗-不曾写在羊皮纸上-不曾侵蚀'
    '也许在我心里-也有一个冬天-一片绝无人迹的雪地',
    '如清晨到夜晚,由山野到书房-只要最后是你,就好.-二零一七',
    '光秃的小树顶-挂着个弯弯的月亮-那是故乡',
    '今夜月明人尽望- -不知秋思落谁家',
    '走到玉林路的尽头-坐在小酒馆的门口-和我在成都的街头走一走',
    '在那座阴雨的小城里-我从未忘记你-成都带不走的,只有你',
]

candidate_4 = [
    '祝你更幸福-更有趣-二零一七',
    '给开发者个新年打赏-一起把美好传递到下一年-二零一七',
    '我行遍世间所有的路,-逆着时光行走,-只为今生与你邂逅',
    '晨风洗去夜和浮尘- -窗角露出澄澈的黎明',
    '春天是远处的故事-白蒙蒙的雪-还没有遮住树梢',
    '给开发者个新年打赏-一起把美好传递到下一年-二零一七',
    '春天是到来的故事-六点钟刚刚敲过-就有人在台阶上跺脚',
    '春天是等待的故事-很亮的银窗纸上-小鸟在睡觉',
    '我耕耘浅浅的诗行-延展着像大西北荒地中-模糊的田垄',
    '灯光-和麦田边新鲜的花朵-正摇荡着黎明的帷幕',
]

candidate_3 = [
    '只要记住你的名字，-不管你在世界的哪个地方，-我一定会去见你。',
    '我会-化作人间的风雨-陪在你身边',
    '我希望有个如你一般的人-如山间清爽的风-如古城温暖的光',
    '我多么希望，有一个门口-早晨，阳光照在草上-二零一七',
    '我想起了海滩, 田野,-眼泪,-笑声.',
    '总有那么一些人-改变着你的习惯-温暖干净',
    '我需要-最狂的风和最静的海-二零一七',
    '有件事我能确信，-假如我们相遇，-肯定能一眼就认出彼此。',
    '我需要-最狂的风-和最静的海',
    '回归文字的本质-回归美好-简诗',
    '最好不相见,如此便可不相恋- -最好不相知,如此便可不相思',
]

candidate_2 = [
    '把小诗分享到微博话题吧-#简诗,回归文字的本质#-等你',
    '回归文字的本质-回归美好-简诗',
    '椿去湫来，海棠花开。-你是否已化作风雨，-穿越时光来到这里。',
    '我会-化作人间的风雨-陪在你身边',
    '只要记住你的名字，-不管你在世界的哪个地方，-我一定会去见你。',
    '黄昏，-不是白昼亦不是夜晚，-是我努力却看不清你的脸。',
    '神明如果真的在的话，-要许下什么愿望才好，-我自己其实也不知道。',
    '有件事我能确信，-假如我们相遇，-肯定能一眼就认出彼此。',
    '自己喜欢的人未必喜欢自己，-人的感情并不是相对的，-这才是有趣之处',
    '谁都不可能和谁在一起一辈子。-人就是这样，-必须去习惯失去。',
    '回归文字的本质-回归美好-简诗',
    '隐约雷鸣，阴霾天空-即使天无雨-我亦留此地',
    '就是因为你不好，-才要留在你身边，-给你幸福。',
    '在两个人的世界里，-管他的风雨雷电飞沙走石天崩地裂，-只要能在一起就足够了。',
    '我们的孤独就像天空中漂浮的城市，-仿佛是一个秘密，-却无从述说。',
    '你不愿意种花，-你说，-我不愿看见它一点点凋落。',
    '我从没被谁知道，所以也没被谁忘记。-在别人的回忆中生活，-并不是我的目的。',
    '我相信，那一切都是种子。-只有经过埋葬，-才有生机。',
    '我想起了海滩, 田野,-眼泪,-笑声.',
    '回归文字的本质-回归美好-简诗',
]

candidate_1 = [
    '樱花落满的梦里，漫寻你的影踪-期盼蓦然的回首-恰吻，你的额头',
    '总有那么一些人-改变着你的习惯-温暖干净',
    '秋凉，添衣-勿念，-速归',
    '此春太凉，彼夏尤伤-今秋勿恼，来冬甚慌-这时光，恰是我思念的模样',
    '你七弦琴流泻的乐声-跌宕，-变幻。',
    '我想起了海滩, 田野,-眼泪,-笑声.',
    '一个眼神-便足以让心海-掠过飓风',
    '我走了，走了一半又停住-等你-等你轻声唤我',
    '回归文字的本质-回归美好-简诗',
    '我们放下尊严,放下个性-放下固执-只是因为放不下一个人',
    '草在结它的种子,风在摇它的叶子,-我们站着，不说话-就十分美好',
    '早晨，黑夜还要流浪-我们把六弦琴交给他-我们不走了',
    '我需要-最狂的风-和最静的海',
    '我想在大地上画满窗子-让所有习惯黑暗的眼睛-都习惯光明',
]
