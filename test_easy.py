import main

easyList = [
	[
		"058409020000060089201030700000013400320080901079000608060005817815700304030090200",
		"062504070300809501105060409531200900027000600009130057000693000700080096400000830",
		"503200100006007802100300705351002084007040610460801000000008561002415070805060000",
		"410060078703501420008473060050094830390010700284300000600000080001940000049028000",
		"489501020750000810000020594008090075500008000001003000160374082000005736003062450",
		"100079080590002734700538009000340020340720051050800003007903508910000300600000190",
		"013420086204600000087010300000030600062500003500764091700040810040800060001256037",
		"007800900096000120200000500410000600908010034063492810000940050801070460540031280",
		"247091068105760300860400007900206000000947680604050019700030920409600000000000403",
		"078410009501020470029060000030007694045300810100000300904672130600000708000831000",
		"010049800080002501200800649000150000740300210006084750370000962400060105000908074",
		"003070005000162004476030019740010000360050007501687002080045926030000850000000473",
		"820300009009750800030080600006230007218547000700090080004105008060070410005904763",
		"048000500005381049000050000803517400169020700054900000516290004402600105000045900",
		"004300001007091240190040800709200506002050030000076912405080000270000158000625370",
		"906800000050049602473206009000132907704590010009000000002015068560007301100600400",
		"400913008905000302600204197001000000250800473309706850102479080598000000000000200",
		"000906000420008600001007208800409517740001930096730020000513060207604000010000459",
		"030100496005096210106000003980670031000000007000031000378415060400763080500928000",
		"823157004000306802169004307000010260400700001500928400048002000070030040001509020",
		"091050680000687005800013020400002000002008760086400100304800250158000340029005071",
		"000345020349706001206001470102079085590000000060000219910007042027913060000000000",
		"501890276040027000807103000096000051008005000050916480002738014100200067000050020",
		"871000340300510006050700091030006009098340002704000508027080900905400600683001200",
		"310605400604210083900030020247560030860100000005302670080000004030000762500070809",
		"107000030096100040200503090028034501703010020410690370072000004001460200009280010",
		"800094075072003908009872630090000700107460020000700100405000387000158402000007016",
		"500000009040015080007003452210760030004098261000032004906071003801040027003000098",
		"060000010042105680097063204026700300050430000403506800605300470730000002200074008",
		"026001000300009257495000010040053100063210740001090030089070001600080429000960308",
		"002080500801257049040003827084190003300705200107032000000078000060009100028500074",
		"501602904609800000827009003406107002218300005750004090074020001080063000000005370",
		"820040060001600890009831507490157000000000000053004000960415008100763200300028051",
		"479012000030670010102900704000040568680000002200863090340080900020400800801520400",
		"000405000009060080500008074000396200032107406106084000080072531057030040603540020",
		"871002040000815006050430001100658079760000500098043060007080003915000000083170200",
		"070405600924060800105008700038057000000000073047090120409602001700830409010549000",
		"500601000030075049000948000157000000096000208200169050410307060020510370703400180",
		"820096007700018000069053200087902400490080063000300908631020009040530000000609801",
		"730805160005200000019060030107300204302519007068004900026100345000003000003650800",
		"902000010005720090037801065170004638080903070000007051003062089000000100291530700",
		"207650000000032000060010542012065094900300600600009380000581260001096453000700910",
		"000807000257049100980031200020000307008062514501370809030496000096700480700000000",
		"506304000490005763087902000023406150050008000100750080275600800030807009000031070",
		"008390705750000096400100000001602984609031207007540000062005078080003020004920001",
		"006250100519607020704900586650001037903720000070040000200000008060530091800160003",
		"096208075200753010050006002070031090000000520500020163010900030003080209900374601",
		"506002070437008000000004538629800045058040720074050091200015000860400010090083000",
		"000034920903002051050180003200047605000006734400050200700301008000060342386400100",
		"005062003000105290900370600602531040030009002049007100100406308096008007284000001",
		"003058009009740062000200538402000013900304087608070250300005020005037090017000340",
		"315600004090000200200590013060175000180300700530040096029051078000030020743002500",
		"074208561002005308100070400001062000040301057000400000090507800218030705003820106",
		"600810270030607940000500630406070003218009704700208060002450000100030490004000516",
		"072031900800009057500820010204003090396210045100006032003000020405960008900004001",
		"218005000490382050000900004004001020080009003002700415007163009649527800500800600",
		"917254000402080000650003400003090256500700309200005071020530760370160098000000030",
		"209700500004090100080030470026001305050000020403050091007003050302015087508427900",
		"409072013702830600016049870200100060547000200690004035803400006000003100060900040",
		"906800000050049602473206009000132907704590010009000000002015068560007301100600400",
		"091050680000687005800013020400002000002008760086400100304800250158000340029005071",
		"906800000050049602473206009000132907704590010009000000002015068560007301100600400",
		"100029003002378015074000008496000050008745096703006080001000670640250000000613500",
		"080072001050031649000040807008050400040000208601200050920763080070010062165900300",
		"020500000649831752500600000003084690018390047006100208080000924074008105060000000",
		"068002479403008000021600530800047913700003004234190087047520001080400020000000000",
		"010086032020009650603000910001543206040020081250100000700005000100070865098001304",
		"802096000005018030106700024078902105000105603001000098984031700250049080600000000",
		"080007001610590800200003640000105400000060208000048003070401902029736100061902074",
		"020170503050000027000650090210407030734800001005031000008704019302000780190086050",
		"000084003130050094905013070400096000003700001750030469504078020360029050020000307",
		"000078005005429000730001090070000020906000507120005936069057081301900060200610450",
		"817000045000051706265003001470568000951000080030090200040200000000005079589730160",
		"400000000100509730000040019204608197000051002003402008305800926706000850801005470",
		"290340000700090265501020090050910072402607051900200600304102000120000040000079023",
		"902000308085600020300000060006517000210030705750804106001062084007450000640301007",
		"090250680005910020043087905407102508080070032900000004304800000150020300600005801",
		"019000000600003040734589610006817430051390000403200000000470103002900867090030020",
		"900830157503106280100740090000050830301004672200013009002070010000000060034060920",
		"000000300820070061360105000050406030093218705482003000270031900005007610000609207",
		"021004830403508201060130000092070540105300000007000008050020300230000086710683450",
		"040071902020009800890050030013400580607000004250083109070002650102000040038704001",
		"250710608903800072087004001062403500079060023000901040005090000706080094801040000",
		"047093508000000040000500190312049600900612700670008019081005926009006800000001073",
		"027500900003100200015304007700201500598043160132000000801960345009000000006037090",
		"201000000067008009005100734080250107509007302020910068170005026903026001000000403",
		"000400087080700490300920010001670040640830275027549030006050020218000700053004000",
		"006050030018300005750280096070020001100063409062000008827009013530000980009830200",
		"062308400185020703070001000000045396090000107700096280531900600049050001020600040",
		"902000010005720090037801065170004638080903070000007051003062089000000100291530700",
		"920340080473801005800706034085009200009000470730060809000000002340000001007254360",
		"009010030000760009073008050720009100906830500005002090694050300802306075050204016",
		"500601000030075049000948000157000000096000208200169050410307060020510370703400180",
		"070004130945610000000057006050030004693040002482106057500370060060000081809500070",
		"420070805070105602061090004904002051050301069610009000802000000090824500040906020",
		"000405000009060080500008074000396200032107406106084000080072531057030040603540020",
		"823157004000306802169004307000010260400700001500928400048002000070030040001509020",
		"003200010010069075096075302060050008080036249070900000001007090000000527827090163",
		"247091068105760300860400007900206000000947680604050019700030920409600000000000403",
		"000687040020003060600250107130000005500002730764038009000300026056001473040720001",
	],
	[
		"658479123743162589291538746586913472324687951179254638962345817815726394437891265",
		"962514378374829561185367429531276984827945613649138257218693745753482196496751832",
		"573284196946157832128396745351672984287549613469831257734928561692415378815763429",
		"415269378763581429928473561157694832396812745284357196672135984831946257549728613",
		"489531627752649813316827594238496175547218369691753248165374982924185736873962451",
		"132479685598162734764538219871345926349726851256891473427913568915687342683254197",
		"913427586254683179687915324479132658162598743538764291726349815345871962891256437",
		"157823946396754128284169573415387692928516734763492815672948351831275469549631287",
		"247391568195768342863425197958216734312947685674853219781534926439672851526189473",
		"378415269561928473429763581832157694745396812196284357984672135613549728257831946",
		"613549827984672531257831649832157496745396218196284753378415962429763185561928374",
		"213479685859162734476538219742913568368254197591687342187345926934726851625891473",
		"827316549649752831531489672496238157218547396753691284374165928962873415185924763",
		"948762531275381649631459827823517496169824753754936218516298374492673185387145962",
		"524368791867591243193742865749213586612859437358476912435187629276934158981625374",
		"926871534851349672473256189685132947734598216219764853342915768568427391197683425",
		"427913568915687342683254197871345926256891473349726851132479685598162734764538219",
		"378926145429158673561347298832469517745281936196735824984513762257694381613872459",
		"832157496745396218196284753984672531613549827257831649378415962429763185561928374",
		"823157694754396812169284357387415269492763581516928473948672135275831946631549728",
		"791254683243687915865913427437162598912538764586479132374891256158726349629345871",
		"871345926349726851256891473132479685598162734764538219915687342427913568683254197",
		"531894276649527138827163945496382751218475693753916482962738514185249367374651829",
		"871269345349518726256734891132856479598347162764192538427685913915423687683971254",
		"312685497674219583958734126247568931863197245195342678781926354439851762526473819",
		"157946832396128745284573196928734561763815429415692378672351984831469257549287613",
		"831694275672513948549872631396281754157469823284735169415926387763158492928347516",
		"568427319342915786197683452219764835734598261685132974926871543851349627473256198",
		"568247913342195687197863254926781345851439726473526891685312479734958162219674538",
		"726531984318649257495827613842753196963218745571496832289374561637185429154962378",
		"672984531831257649549613827284196753396745218157832496415378962763429185928561374",
		"531672984649831257827549613496157832218396745753284196374928561185763429962415378",
		"827549163531672894649831527496157382218396475753284916962415738185763249374928651",
		"479312685538674219162958734913247568687195342254863197345781926726439851891526473",
		"378415962429763185561928374745396218832157496196284753984672531257831649613549827",
		"871962345349815726256437891132658479764291538598743162427586913915324687683179254",
		"873415692924763815165928734238157946691284573547396128489672351752831469316549287",
		"549631827831275649672948531157823496396754218284169753415387962928516374763492185",
		"823496157754218396169753284387962415492185763516374928631827549948531672275649831",
		"734895162685231479219467538197386254342519687568724913926178345851943726473652891",
		"962345817815726394437891265179254638586913472324687951743162589658479123291538746",
		"247658139195432876863917542312865794958374621674129385439581267781296453526743918",
		"613827945257649138984531276429185367378962514561374829832496751196753482745218693",
		"516374928492185763387962415823496157754218396169753284275649831631827549948531672",
		"218396745753284196496157832531672984649831257827549613962415378185763429374928561",
		"386254179519687324724913586652891437943726815178345962231479658467538291895162743",
		"396218475284753916157496382672531894831649527549827163415962738763185249928374651",
		"586132479437598162912764538629871345158349726374256891243915687865427913791683254",
		"178534926943672851652189473231947685895216734467853219724391568519768342386425197",
		"415962783763185294928374615672531849831649572549827136157496328396218457284753961",
		"123658479589743162746291538472586913951324687638179254394815726265437891817962345",
		"315627984496813257278594613964175832182369745537248196629451378851736429743982561",
		"374298561962145378185673429531762984649381257827459613496517832218936745753824196",
		"649813275531627948827594631496175823218369754753248169962451387185736492374982516",
		"672531984831649257549827613284753196396218745157496832763185429415962378928374561",
		"218475396496382157753916284374651928185249763962738415827163549649527831531894672",
		"917254683432687915658913427743891256581726349296345871129538764374162598865479132",
		"219764538734598162685132479926871345851349726473256891197683254342915687568427913",
		"489672513752831694316549872238157469547396281691284735873415926924763158165928347",
		"926871534851349672473256189685132947734598216219764853342915768568427391197683425",
		"791254683243687915865913427437162598912538764586479132374891256158726349629345871",
		"926871534851349672473256189685132947734598216219764853342915768568427391197683425",
		"185429763962378415374561928496832157218745396753196284531984672649257831827613549",
		"489672531752831649316549827238157496547396218691284753924763185873415962165928374",
		"827549316649831752531672489753284691218396547496157238185763924374928165962415873",
		"568312479473958162921674538856247913719863254234195687347526891185439726692781345",
		"915786432427319658683452917871543296349627581256198743764835129132974865598261374",
		"832496517745218936196753824378962145429185673561374298984531762257649381613827459",
		"984627531613594827257813649832175496745369218196248753378451962429736185561982374",
		"926178543851943627473652198219467835734895261685231974568724319342519786197386452",
		"276984513138257694945613872482196735693745281751832469514378926367429158829561347",
		"692378145815429673734561298573196824946832517128745936469257381351984762287613459",
		"817926345394851726265473891472568913951342687638197254746219538123685479589734162",
		"479123685162589734538746219254638197687951342913472568345817926726394851891265473",
		"296345817743891265581726394658913472432687951917254638374162589129538746865479123",
		"962145378185673429374298561496517832218936745753824196531762984827459613649381257",
		"791254683865913427243687915437162598586479132912538764374891256158726349629345871",
		"219746358685123749734589612926817435851394276473265981568472193342951867197638524",
		"946832157573196284128745396469257831351984672287613549692378415815429763734561928",
		"514962378829374561367185429751496832693218745482753196276531984945827613138649257",
		"921764835473598261568132974692871543185349627347256198856427319234915786719683452",
		"345871962726349815891256437913427586687915324254683179479132658162598743538764291",
		"254719638913856472687234951162473589479568123538921746345692817726185394891347265",
		"247193568195867342863524197312749685958612734674358219781435926439276851526981473",
		"427586913683179254915324687764291538598743162132658479871962345349815726256437891",
		"231479685467538219895162734386254197519687342724913568178345926943726851652891473",
		"962415387185763492374928516531672948649831275827549631496157823218396754753284169",
		"496157832218396745753284196374928561185763429962415378827549613531672984649831257",
		"962378415185429763374561928218745396496832157753196284531984672649257831827613549",
		"962345817815726394437891265179254638586913472324687951743162589658479123291538746",
		"926345187473891625851726934685479213219538476734162859568913742342687591197254368",
		"269415738581763249473928651728549163946831527135672894694157382812396475357284916",
		"549631827831275649672948531157823496396754218284169753415387962928516374763492185",
		"276984135945613728138257946751832694693745812482196357514378269367429581829561473",
		"429673815378145692561298734984762351257381469613459287832517946196824573745936128",
		"378415962429763185561928374745396218832157496196284753984672531257831649613549827",
		"823157694754396812169284357387415269492763581516928473948672135275831946631549728",
		"753248916218369475496175382962451738185736249374982651531627894649813527827594163",
		"247391568195768342863425197958216734312947685674853219781534926439672851526189473",
		"915687342427913568683254197132479685598162734764538219871345926256891473349726851",
	]
]

for index, easy in enumerate(easyList[0], start=0):
	result = main.sudokuLine(easy)
	print("Easy test " + str(index + 1) + " " + ("PASS" if result == easyList[1][index] else "FAIL"))
	# print(easy)
	# print(result)