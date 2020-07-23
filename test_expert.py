import main

expertList = [
	[
		"000506000000000062704010000900043007020000000080090050000000000300008700050304001",
		"204000000107090002000000700600001000000020603801049000400060070000000009000300560",
		"030000080500060000000008219007900060000007002000200100071340000200000403009000000",
		"060000000000509807100086000000000002000031700009400300403000000801940000000000035",
		"005002000700000000009700000100080200300010600060000903000870040050040706003006000",
		"000071020000000800098200000780900300000007000050003000004100685000000009200090004",
		"030000080000100207028040000004000030800090000057400100001007400009000308000000060",
		"030000080000100207028040000004000030800090000057400100001007400009000308000000060",
		"000070030005000100080309000503027080600000007002500000000450008040000060000006009",
		"500904000600000001800600009000000007200700300030090000007500020000409060020300400",
		"032700000008000004000000010400090508600504100000007002000005000000080473009006000",
		"007930008680005090000000002000400080500106030060000000001054000009700001000000070",
		"020000000001009700403000800302005000000007910000600004680000400000700030000500002",
		"000004007020010950600200000006800010050100408200000600000070000180000000004060090",
		"700080000005020009000000300500400000002000860100000004020007400000090200403005001",
		"003029001600100400008370000904000000061000058000002000050000060000860040700000000",
		"002000000000000913090300050000180040000004720073000000700000000010070000680000409",
		"030400500670005002040000100000870900800006003002000000007002005000090730000000009",
		"000040026309720000050000400007913000603000000000000002100000080000008009090000704",
		"000008500001000000473600000600200004000007030000095060000000006107080000008704000",
		"020608009700001500500000002000002345090010006005007000070000910000300000600000000",
		"006300070001700309000090200000000010000900007097050000080000000030062500010008060",
		"003200000000000807600900530009040200075002090000000050401000000080561000700000000",
		"008209000100000000470005030005000001800400006020800000000500420007000900000097080",
		"000680000060000500500030000000920000006000001340000006010300007007000900080090250",
		"004001076000009100000800005030000001740200000190003400000000300000304020008060000",
		"000540001009800270001000000060015000000060090304000010400000800200096700050000000",
		"000090000762000000000800300000009200030000007804005001100000070000100004290007005",
		"530072008609000000000000001050000160200390000400100800000060490000005000074000000",
		"063000008908500000000070000000004500830050090009610000050030460000000000200100030",
		"900000007004000010000700092750008000200000000000170020500020000600000070000004631",
		"000090010200000050680000000060400103000905800107000004000800400000300006400050000",
		"000270010300059000090800204685000009004000000000000030900000000001090720000500800",
		"080000030704000000000500060001006000900340000070800200008003420040000910000250000",
		"008007900042005000000600050003006801000000006900070000080130470000090000010000000",
		"009081000070200040050003000030060409008000002000009000400600010000400087000000050",
		"000600000508000001000091005000000503340800600000407000900324000007000010600000002",
		"805070020000100000000030000200300800000020090040000065010050000430087000600000070",
		"100004600700003000000050000000045000600000050307190200000500900080020003060070400",
		"000006000000109500680000090002700080090000004004085000000000403000060000870053900",
		"050000009340000060800020000000600000090030100000009503400008001000302078600000040",
		"002080700000004020004000080800006000000001060050073900000000130000090500900040000",
		"070000608102000000030700000000420006000005020000000170305000000000256400700009010",
		"080001069000000000016400000004206000000130000000000802038000000040007050000029047",
		"370004090001000000000017000000060000960300057080000003500000429030008060200000000",
		"000500090030000005000827000100406000090000070280050000405000000700000902000000156",
		"005800906276300000000000000100420000000010302004000090000000080000598700300000010",
		"400000100000002007083090000070006400040001000000000081000000000500030002100080709",
		"000007081500004000020003000080000073060000000004560200400800017010000000000090020",
		"000000032018000000000804006000140000080070400370200000001000000600000257020000603",
		"060000005900001000010070002602004030000050040040010000007002006200090700300000010",
		"108000005000000020000403090720068000009000600000100000030000400890700000000210500",
		"020070400740060000050009060000000600006000031070003500000090204100005000000000007",
		"050090010000000700000050406908002000070800000600540020000000062000703100506000000",
		"073200100000090000006150020000400087000003002004900500001070940060000000080000000",
		"002085004000030060004210030000000052000000310900000000800006000250400008000001600",
		"090000000000000460200000005070804010030020000500060800010730020908050000000200000",
		"007008000095002600000100250010000079600009000008004000000000000006400800030050020",
		"000010000020000095070050003002300701000700400430800000650400000000062000090000070",
		"405000008000100000900070560602000004000600000509000003007000800000200700084003000",
		"000901600508000000007600050000004000000000801906000000005000400000700000030009162",
		"005002000000040010006030000090000032002000740307000000000020501080700009060010008",
		"102004005008000730000000000007300500080000000000006042000000070040620001000503900",
		"400800100010000300700096000800600040000050000031000072300000900062000400000400060",
		"400050800018000700003004000960000000005003000070008060001600004000500013000800000",
		"000000027080000500000831000000090010000007090006280000400700180370405000000020000",
		"000078500004000020100000067000000900000900070640200008008000000700106002090000050",
		"672500000000000000000049000010000070003085400900000560000200000200703090050000830",
		"050670000600040100000030008103007000040003200000000730000000006005800400300002050",
		"006040030030000609000130800020000070000294005010000900000328000600000000400000050",
		"560720000090006000000000800004800600000000009000060050000178400050040070403000000",
		"904000206050049000000000000300002010061000009000085000000000050700218000190700000",
		"070000608102000000030700000000420006000005020000000170305000000000256400700009010",
		"030600890000040000000800507090000000000006405300004010060010030001000200400020000",
		"508000300002950000000000000700009006600003040019700000000007004800000070003200180",
		"000500090030000005000827000100406000090000070280050000405000000700000902000000156",
		"000300000070000000009085063900000670000040030010820009005000090000006100100000004",
		"000000090003000708000600005000590006100700000850002040009070000008300600004000180",
		"000123000000000700008000010000070560060000042020008000430000006006090800000005003",
		"000007000002900600107600050400200091000000000800300020030500000605030400009000008",
		"000500000005002940006000070000050020007004100800390000403000006000400007080060002",
		"000010920000493000000000070600000300050000000013000068002900730400000005508007000",
		"000083090607000300010000000070100085000590000008700000040071000006000050800000003",
		"040027031000800000130004000320070400050000018000000050600980000000000005700000060",
		"800400010003905600001600000400500060010000038006030070000000000009000005070006000",
		"080000090010086302000310000004000000000000005000261004000540006309000800200000000",
		"000000000302900007090038050004000060080000009010746500900010000050004000000005090",
		"007010065900700200080000000090001007004000910030000000001040029000020050050000300",
		"000307000010400600700000090900000507073160004000000006080001400060075000000000002",
		"090030001700090000008000960500004000000200018800600000060000054000020007004001000",
		"720500000500040600080100000000003009043000000000006050001600407000009000090000020",
		"900005070000008500100700020090057000200000040053200000800000603040030050000000900",
		"090007008007000000000803910612008300000000060000000020400080200001006000070400001",
		"003004058600100002204000000079000000100080300000600000305008090020090001800000000",
		"700920060002000000005003409300600980000801000007040000900000830020000000000004100",
		"002090600000040003100008000730000002080000400000000008900000005050034020000620001",
		"005060030000100009020300050100000002006008405004000010070000800000049000000807100",
		"900000000800004700403065001000000050002900080008070003600000470030000002010006000",
		"600170005000040020000000890037800002500001009002000000005024000000010600700300000",
		"910000060000005000050003090002090400079000000030064000700000058000001000000250304",
	],
	[
		"132586479598437162764912538915243687427865913683791254871629345349158726256374891",
		"284753196157496832396218745672531984549827613831649257415962378763185429928374561",
		"132479685598162734764538219427913568915687342683254197871345926256891473349726851",
		"568724193342519867197386524734895612685231749219467358473652981851943276926178435",
		"685132479734598162219764538197683254342915687568427913926871345851349726473256891",
		"543871926627349851198256473786915342319427568452683197974132685835764219261598734",
		"135276984946138257728945613694751832812693745357482196581367429269514378473829561",
		"135276984946138257728945613694751832812693745357482196581367429269514378473829561",
		"469175832735248196281369745513627984694813257872594613926451378347982561158736429",
		"513984672694257831872613549469832157281745396735196284347561928158429763926378415",
		"132749685598612734764358219427193568683524197915867342871435926256981473349276851",
		"427931568683245197915678342132497685598126734764583219871354926349762851256819473",
		"926871345851349726473256891342915687568427913197683254685132479219764538734598162",
		"531984267827613954649257183496832715753196428218745639962378541185429376374561892",
		"734589612685123749219746358568472193342951867197638524926817435851394276473265981",
		"543629781627158439198374526974586312261437958835912674452791863319865247786243195",
		"342591687568742913197368254926187345851934726473625891734859162219476538685213479",
		"931427568678915342245683197354871926819256473762349851497132685126598734583764219",
		"871345926349726851256891473427913568683254197915687342132479685764538219598162734",
		"926178543851943627473652198685231974219467835734895261342519786197386452568724319",
		"123658479746291538589743162817962345394815726265437891472586913951324687638179254",
		"926345871851726349473891256342687915568913427197254683685479132734162598219538764",
		"813257649594613827627984531369745218175832496248196753451378962982561374736429185",
		"538219764162734598479685132345926871891473256726851349913568427687342915254197683",
		"132685479764219538598734162871926345256473891349851726915342687427568913683197254",
		"984531276257649138613827945832496751745218693196753482429185367561374829378962514",
		"827549631649831275531672948962415387185763492374928516496157823218396754753284169",
		"381694752762513489459872316517469238936281547824735691145926873673158924298347165",
		"531672948649831275827549631753284169218396754496157823185763492962415387374928516",
		"763429158928561347415378926672984513831257694549613872157832469396745281284196735",
		"962451387374982516185736492753248169218369754496175823531627948649813275827594631",
		"734598612219764358685132749568427193342915867197683524926871435851349276473256981",
		"568274913342159687197836254685321479734985162219647538926718345851493726473562891",
		"685479132734162598219538764851726349926345871473891256568913427342687915197254683",
		"568427913342915687197683254473256891851349726926871345685132479734598162219764538",
		"349581726871296345256743891132865479598374162764129538427658913915432687683917254",
		"132658974598743261764291835871962543349815627256437198915324786427586319683179452",
		"865479123374162589129538746296345817581726394743891265917254638432687951658913472",
		"135984672728613549946257831812745396694832157357196284473561928581429763269378415",
		"915876342427139568683542197132794685598621734764385219256918473349267851871453926",
		"256473819349851762871926354132685497598734126764219583427568931915342678683197245",
		"132685794598734621764219385871926453349851267256473918427568139683197542915342876",
		"479132658162598743538764291913427586687915324254683179345871962891256437726349815",
		"382751469475693281916482735894276513527138694163945872738514926249367158651829347",
		"375824196821936745649517832153762984964381257782459613518673429437298561296145378",
		"672531498831649725549827361157496283396218574284753619415962837763185942928374156",
		"435871926276349851981256473193427568867915342524683197749132685612598734358764219",
		"427568193915342867683197524871926435349851276256473981764219358598734612132685749",
		"649257381531984762827613459185429673962378145374561298496832517218745936753196824",
		"496517832218936745753824196962145378185673429374298561531762984649381257827459613",
		"763429185928561374415378962672984531831257649549613827157832496284196753396745218",
		"178926345943851726652473891724568913519342687386197254231685479895734162467219538",
		"629378415743561928851429763315984672496257831278613549537196284182745396964832157",
		"754396218169284753823157496948672531275831649631549827387415962492763185516928374",
		"573284169128396754946157823692415387815763492734928516351672948469831275287549631",
		"132685974598734261764219835683197452427568319915342786871926543256473198349851627",
		"396475281157382469284916735672894513831527694549163872415738926928651347763249158",
		"247568913195342687863197254312685479674219538958734162781926345526473891439851726",
		"586913247324687195179254863962345781815726439437891526658479312743162958291538674",
		"415962378763185429928374561672531984831649257549827613157496832396218745284753196",
		"342951687568472913197638254851394726473265891926817345685123479219746538734589162",
		"135672984728549613946831257694157832812396745357284196473928561581763429269415378",
		"132974685598261734764835219427319568683452197915786342256198473349627851871543926",
		"496832157218745396753196284827613549649257831531984672374561928962378415185429763",
		"496157832218396745753284196962415378185763429374928561531672984827549613649831257",
		"613549827984672531257831649745396218832157496196284753429763185378415962561928374",
		"962378514374561829185429367827613945531984276649257138218745693753196482496832751",
		"672531984549827613831649257415962378763185429928374561396218745284753196157496832",
		"951678342638245197472931568123497685746583219589126734817354926265819473394762851",
		"276849531138572649945136827829615374367294185514783962751328496693457218482961753",
		"568724193197386524342519867734895612685231749219467358926178435851943276473652981",
		"984531276257649138613827945378962514561374829429185367832496751745218693196753482",
		"479132658162598743538764291913427586687915324254683179345871962891256437726349815",
		"135672894728549163946831527694157382812396475357284916269415738581763249473928651",
		"568472391342951768197638425734589216685123947219746853926817534851394672473265189",
		"672531498831649725549827361157496283396218574284753619415962837763185942928374156",
		"561374928378962415429185763984531672257649831613827549745218396832496157196753284",
		"685427391423915768971683425347598216192764853856132947269871534518349672734256189",
		"749123685612589734358746219193472568867951342524638197435817926276394851981265473",
		"568427913342915687197683254473256891926871345851349726734598162685132479219764538",
		"728549631135672948946831275694157823357284169812396754473928516269415387581763492",
		"345718926726493851891562473687159342254836197913274568162985734479321685538647219",
		"254683197687915342913427568479132685162598734538764219345871926726349851891256473",
		"849627531572813649136594827328175496457369218961248753615982374294736185783451962",
		"865427913243915687791683254437598162912764538586132479158349726629871345374256891",
		"683452197915786342427319568764835219132974685598261734871543926349627851256198473",
		"568472913342951687197638254734589162685123479219746538926817345851394726473265891",
		"427319865915786243683452791598261437764835912132974586871543629349627158256198374",
		"692387145815492673734516298946823517573169824128754936287631459469275381351948762",
		"496832571753196842218745963531984726649257318827613495962378154185429637374561289",
		"724568931519342678386197245652473819943851762178926354231685497467219583895734126",
		"962415378374928561185763429496157832218396745753284196827549613649831257531672984",
		"193247658867195432524863917612958374749312865358674129435781296981526743276439581",
		"913274658687159432254836917479321865162985374538647129345718296726493581891562743",
		"734928561692415378815763429351672984469831257287549613946157832128396745573284196",
		"342591687568742913197368254734859162685213479219476538926187345851934726473625891",
		"415962738763185249928374651157496382396218475284753916672531894831649527549827163",
		"926817345851394726473265891197638254342951687568472913685123479734589162219746538",
		"629178345158943726374652891437895162586231479912467538865724913243519687791386254",
		"913427865687915243254683791162598437479132586538764912726349158345871629891256374",
	]
]

for index, expert in enumerate(expertList[0], start=0):
	result = main.sudokuLine(expert)
	print("Expert test " + str(index + 1) + " " + ("PASS" if result == expertList[1][index] else "FAIL"))
	# print(expert)
	# print(result)