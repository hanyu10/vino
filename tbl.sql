-- --------------------------------------------------------
-- 호스트:                          database-vino.c8bzsodzz3ov.ap-northeast-2.rds.amazonaws.com
-- 서버 버전:                        10.4.13-MariaDB-log - Source distribution
-- 서버 OS:                        Linux
-- HeidiSQL 버전:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- 테이블 데이터 dbvino.wine_wine:~41 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wine_wine` DISABLE KEYS */;
INSERT IGNORE INTO `wine_wine` (`id`, `name`, `food`, `wine_type`, `sugar`, `sour`, `kind`, `region`, `explain`, `area_id`) VALUES
	(1, 'Serra, Organic Brut Cava', 'Cheese', 'Sparkling', 1, 4, '마카베오', '페네데스(Penedes)', '밝은 볏짚색을 띠고 청사과, 시트러스의 아로마가 느껴지며 작고 미세한 버블들이 올라온다. 입 안에서는 탄탄한 구조감에 신선한 맛이 깔끔한 와인이다.', 4),
	(2, 'Cantine Povero, Moscato d\'Asti\'Campo del Palio\'', 'Lamb', 'White', 4, 2, '모스카토 100%', '피에몬테(Piemonte) > 아스티(Asti)', '진한 황금 빛의 컬러를 띄며 섬세하고 오래 지속되는 기포가 인상적인 와인이다. 달콤하면서도 신선한 과실의 맛이 오랜 여운으로 남는다.', 3),
	(3, 'Frescobaldi, Pomino Pinot Nero', 'Beef', 'Red', 1, 4, '피노 누아', '토스카나(Toscana)', '까시스와 잘 익은 체리, 초콜렛 향이 퍼지며 입 안에서는 레드 베리 향과 감초, 지중해 허브가 조화를 이루며 긴 피니쉬가 특징적인 와인이다.', 3),
	(4, 'Tinazzi, Primitivo', 'Pasta', 'Red', 1, 3, '프리미티보', '뿔리아(Puglia)', '강렬한 붉은 빛을 띠고 체리와 푸룬 향이 풍미에서도 느껴진다. 입 안에서는 부드러운 타닌과 긴 피니시가 특징적인 와인이다.', 4),
	(5, 'Collalbrigo, Prosecco DOCG Brut', 'Beef', 'Sparkling', 1, 5, '글레라', '베네토(Veneto) > 꼬넬리아노(Conegliano)', '콜라브리고 프로세코 DOCG 의 빈야드는 유네스코 세계 문화유산 보호지역(UNESCO World Heritage Site) 으로 지정된 코넬리아노 발도비아데네(Conegliano Valdobbi-adene) 내에 위치한다. 돌로미테스(Dolomites) 빙하의 이동으로 형성된 언덕에 위치하는 이 빈야드의 생산량은 극히 제한적이다.', 4),
	(6, 'Frescobaldi, Alie Rose', 'Fish', 'Rose', 1, 3, '시라/쉬라즈, 베르멘티노', '토스카나(Toscana)', '그윽하고 섬세하며 복숭아 향과 장미향이 어우러진다. 입 안에서는 핑크 자몽의 시트러스 향이 부드럽게 채우는 와인이다.', 3),
	(7, 'Masca del Tacco, \' Ro’Si \' Pinot Nero Rosato', 'Lamb', 'Rose', 1, 3, '피노 네로', '뿔리아(Puglia)', '밟은 옅은 분홍색에 야생 딸기 젤리 수박과 같은 달콤한 향이 풍부하고 그 뒤로 향신료 광물 미네랄 향이 희미하게 돈다. 입 안에서는 부드럽고 쥬시하게 감싸고 신선하지만 우아한 과실향이 길게 여운으로 남는 와인이다.', 3),
	(8, 'Allegrini, Lugana', 'Fish', 'White', 1, 4, '투르비아노, 코르테제', '베네토(Veneto) > 베로나(Verona) > 루가나(Lugana)', '연두빛이 비치는 연한 볏짚색을 띠고 우아한 꽃향과 함께 아몬드향이 은은하게 어우러진다. 입 안에서는 우아하면서도 신선한 풍미를 가지고 있는 와인이다.', 3),
	(9, 'Cantina Colli Euganei, Prosecco Frizzante', 'Cheese', 'White', 1, 4, '글레라', '밀짚 Yellow색상으로 지속적으로 이어지는 기포와 좋은 과실향이 조화로운 세미 스파클링이다.', '밀짚 Yellow색상으로 지속적으로 이어지는 기포와 좋은 과실향이 조화로운 세미 스파클링이다.', 3),
	(10, 'Cuvage, Acquesi Rosato', 'Chicken', 'Sparkling', 1, 3, '바르베라 70%, 돌체토 30%', '피에몬테(Piemonte)', '핑크빛을 띠고 장미꽃의 아로마가 느껴진다. 입 안에서는 로제의 우아하고 상큼하며 깔끔한 맛에 기품있는 버블이 고급스러운 와인이다.', 3),
	(11, 'Castellare, Poggio Al Merli', 'Lamb', 'Red', 1, 3, '메를로 100%', '토스카나(Toscana)', '', 3),
	(12, 'Pedralonga, DoUmia', 'Lamb', 'Red', 1, 3, '멘시아, 카이노 틴토, 에스파데이로', '리아스 바이사스(Rias Baixas)', '매우 짙은 붉은색을 띠고 첫 향에서부터 느껴지는 나무 향 Woody와 숲 바닥의 흙 냄새 Forest Floor aromas는 아주 진한 으깬 라즈베리 Crushed Raspberries, 장미 꽃잎 Rose petal, 야생 체리 Wild Cherry, 커피 Coffee, 엽궐련 Tobacco 등의 다양한 아로마들과 함께 와인 잔을 가득 채운다. 입 안에서의 목 넘김 후 느껴지는 짠 미네랄 Salty mineral은 이 와인이 생산된 지역의 정체성을 보여준다.', 4),
	(13, 'Alejandro Fernandez, 20 Aldeas', 'Lamb', 'Red', 1, 3, '템프라니요', '리베라 델 두에로(Ribera del Duero)', '블랙커런트, 블랙베리 등 검은 과실의 진한 아로마와 템프라니요 품종 특유의 감초 향이 느껴지며, 미국산 배럴에서 숙성해 자연스럽게 배어나는 바닐라, 커피, 캐러멜, 스모키한 향이 어우러진다. 입 안에서는 잘 다듬어진 풍성한 타닌과 적절한 산도가 균형을 이루어 기분 좋은 여운을 남기는 와인이다.', 4),
	(14, 'Casa Rojo, La Gabacha', 'Fish', 'White', 1, 3, '소비뇽 블랑', '루에다(Rueda)', '연한 골드빛을 띠고 오픈했을 때는 망고,파인애플과 함께 레몬향이 어우러진다. 잔디향과 같은 소비뇽블랑 품종의 특징적인 향이 강렬하게 느껴진다. 입 안에서는 높은 산도와 당도의 밸런스가 뛰어난 와인이다.', 4),
	(15, 'Piqueras, Wild Femented Verdejo', 'Cheese', 'White', 1, 2, '베르데호 100%', '알만사(Almansa)', '밝은 금색의 노란 컬러로 복합적이고 잘익은 열대과실, 미네랄, 그리고 약간의 삼나무의 아로마가 느껴진다. 입안에선 묵직하고 세련된 자연스러운 산도가 좋은 균형감을 주고 긴 피니쉬가 매력적인 가격대비 품질이 뛰어난 와인이다.', 4),
	(16, 'Las Moradas, Initio', 'Cheese', 'Red', 1, 4, '가르나차', '비노스 데 마드리드(Vinos de Madrid)', '살짝 가넷 빛이 올라오는 깨끗하고 밝은 루비색에 블랙베리, 자두, 오렌지 꽃, 코코아, 야생허브, 감초, 미네랄 등을 느낄 수 있는 매우 복합적인 와인이다. 입 안에서는 산미가 워낙 좋아서 생동감이 느껴지며, 우아하고, 탄탄한 구조에 오래도록 지속되는 여운을 지니고 있는 와인이다.', 4),
	(17, 'Pago Ayles, Cuesta del Herrero', 'Beef', 'Red', 1, 3, '가르나차 , 템프라니요, 카베르네 소비뇽, 메를로', '', '매혹적인 짙고 깊은 루비 컬러을 띠고 신선한 붉은 과실 향과 함께 잉크, 스파이시 향이 어우러지며 꽃 향으로 마무리 된다. 입 안에서는 잘 익은 과육의 맛이 우아하고 인상적이고 조화롭게 균형 잡힌 맛이 적당한 타닌감과 중간 이상의 바디감이 입 안을 가득 메우며 풍부한 피니쉬를 남기는 와인이다.', 4),
	(18, 'Bodegas San Valero, Origium Garnacha', 'Beef', 'Red', 1, 3, '가르나차', '까리레나(Carinena)', '잘 익은 체리, 딸기류 과실향과 풍부한 아로마가 느껴지고 입 안에서는 적절한 산도가 조화로운 레드 와인이다.', 4),
	(19, 'Bodegas San Valero, Gran Ducay CAVA Brut Nature', 'Fish', 'Sparkling', 1, 4, '마카베오, 빠레야다, 자렐로', '까리레나(Carinena)', '프랑스 샴페인 방식으로 양조되어 끈임없이 발생하는 미세한 기포가 상큼한 시트러스향과 함께 상쾌하게 느껴지는 가성비 최고의 까바(스파클링 와인)다. 병입 후 9개월간 숙성했다.', 4),
	(20, 'Senorio de Iniesta, Rosado Bobal', 'Pasta', 'Rose', 1, 3, '보발 100%', '만추엘라(Manchuela)', '진한 체리핑크 빛과 사랑스러운 로즈 컬러를 띠며 보발 품종의 특징적인 야생 딸기와 붉은 과일 향이 향긋하게 피어난다. 프레쉬한 매력을 주는 산도와 함께 과일 바구니와 같은 기분 좋은 아로마가 입에서도 이어진다. 봄철 피크닉이나 가벼운 음식을 함께한 홈파티에서 즐기기 좋은 와인이다.', 4),
	(21, 'Lustau, Amontillado Los Arcos Solera Reserva', 'Cheese', 'Fortified', 1, 0, '팔로미노 100%', '헤레즈-헤레스-셰리(Jerez-Xeres-Sherry)', '셰리(Sherry)는 스페인의 대표적인 주정강화와인(Fortified Wine)이자 헤레스(Jerez)의 영어식 이름이다. 원산지 명칭 보호에 포함되어 있어서 ‘셰리’라는 이름을 라벨에 붙이려면 모두 헤레스 데 라 프론테라, 산루카 데 바라메다, 엘 푸에르토 데 산타마리아 지역에서 생산한 것이어야 한다. 발효 도중에 강화하는 포트 와인과는 달리 발효가 완료된 화이트 와인에 브랜디를 섞어 알코올을 높인다.', 4),
	(22, 'Chateau Courac, Cotes du Rhone Villages Laudun Bla', 'Lamb', 'Red', 1, 3, '클레렛, 그르나슈 블랑', '론(Rhone) > 꼬뜨 뒤 론(Cotes du Rhone)', '황금빛 컬러와 열대과일의 향, 복합 미가 매력적이고 입 안을 감싸는 균형미와 오랫동안 남는 아로마의 여운이 아주 훌륭하다. 와인메이커는 끌라레뜨라는 전통적인 품종 블랜딩을 고수하고 있는데, 덕분에 풍성한 꽃향기와 미네랄리티를 가진 우아한 화이트 와인의 모습을 보여준다. 실크 같은 질감과 풍성한 느낌의 와인으로 무엇보다 신선함이 마무리까지 입안을 즐겁게 하는 와인이다.', 2),
	(23, 'Chateau Courac, Cotes du Rhone Villages Laudun Rou', 'Beef', 'Red', 1, 3, '시라/쉬라즈, 그르나슈, 무르베드르, 쿠누아즈', '론(Rhone) > 꼬뜨 뒤 론(Cotes du Rhone)', '강렬한 루비 컬러에 첫인상은 잘 익은 붉은 과일이 가득한 바구니의 향을 맡는 것처럼 직관적으로 느껴진다. 잔 안에서 시간이 지날수록 신선함과 훌륭한 구조감을 보여주며 그 속에서 감초의 노트도 느껴진다. 입 안에서는 실크같이 부드러운 타닌과 피니쉬까지 잘 익은 과일이 연상되는 아로마가 긴 여운을 남기는 와인이다.', 2),
	(24, 'Chateau Courac, Cotes du Rhone', 'Cheese', 'Red', 1, 3, '그르나슈, 시라/쉬라즈, 쌩쏘, 까리냥', '론(Rhone) > 꼬뜨 뒤 론(Cotes du Rhone)', '짙은 루비색을 띠고 신선한 라즈베리와 체리 같은 붉은 과실의 아로마를 강렬하게 풍긴다. 입 안을 가득 채운 아름다운 아로마는 지속적으로 강렬하면서 생동감 넘치는 모습을 보여주는 와인이다.', 2),
	(25, 'Thomas Kim Desruets Brut', 'Pasta', 'Sparkling', 1, 4, '피노누아, 샤르도네, 피노 뮈니에', '샹파뉴(Champagne)', '황금빛을 띠며 미세한 기포가 오랜 시간 동안 올라오고 푹 익은 사과향과 짙은 버터향, 고소한 견과류, 흰 꽃 계열의 아로마가 느껴진다. 적당한 도사지로 달콤한 꿀과 갓 구운 브리오슈 빵을 먹는듯한 고소함에 쌉싸르함이 더해져 계속해서 마시고 싶어지는 프리미엄 샴페인이다.', 2),
	(26, 'Calmel & Joseph, Villa Blanche Chardonnay', 'Fish', 'White', 1, 3, '샤르도네', '서던 프랑스(Southern France) > 랑그독 루씨용(Languedoc Roussillon)', '밝은 황금색을 띠고 살구, 복숭아 등의 신선한 과일 아로마가 두드러지며 엘더베리, 아니스, 민트, 흰 꽃 등의 다채로운 향이 덧입혀진다. 입 안에서는 열대과일의 농축된 풍미와 신선한 산미, 은은한 오크 뉘앙스, 짭쪼롬한 여운이 길게 남는 와인이다.', 2),
	(27, 'Calmel & Joseph, Villa Blanche Grenache Rose', 'Cheese', 'Rose', 1, 3, '그르나슈 그리, 그르나슈', '프랑스(France) > 서던 프랑스(Southern France) > 랑그독 루씨용(Languedoc Roussillon)', '밝고 연한 핑크색을 띤 드라이 로제 와인으로, 장미꽃, 흰 꽃, 아니스 열매 등 다채로운 아로마가 화사한 스타일이다. 입 안에서 복숭아, 살구 등 흰 과일의 프루티한 맛과 시트러스 같은 활기찬 산미의 균형을 즐길 수 있고 아몬트, 민트 등의 터치가 은은하게 여운으로 남는 와인이다.', 2),
	(28, 'Calmel & Joseph, La Madone', 'Beef', 'Red', 1, 3, '그르나슈, 시라/쉬라즈', '서던 프랑스(Southern France) > 랑그독 루씨용(Languedoc Roussillon)', '매혹적인 가넷색을 띠고 블랙 커런트, 블랙베리 등의 과일 향과 시나몬 등 향신료 향이 조화롭게 어우러진다. 입 안에서는 파워풀하면서 우아한 캐릭터를 보여주며 검붉은 과일과 향신료, 자잘한 타닌감이 느껴지고 기본 좋은 여운이 길게 남는 와인이다.', 2),
	(29, 'Calmel & Joseph, Les Terroirs, Cotes du Roussillon', 'Cheese', 'Red', 1, 3, '그르나슈, 시라/쉬라즈, 까리냥', '서던 프랑스(Southern France) > 랑그독 루씨용(Languedoc Roussillon)', '블랙베리 같은 검은 과일의 아로마가 진하게 피어오르고 시나몬, 코코아, 달콤한 향신료 향이 함께 나타난다. 입 안에서는 잘 녹아든 타닌의 부드러운 감촉을 즐길 수 있으며 블랙커런트, 후추, 시나몬, 감초, 민트 등 다양한 풍미가 긴 여운을 남기는 와인이다.', 2),
	(30, 'Calmel & Joseph, Les Terroirs, Corbieres', 'Cheese', 'Red', 1, 3, '그르나슈, 시라/쉬라즈', '서던 프랑스(Southern France) > 랑그독 루씨용(Languedoc Roussillon)', '붉은 과일 아로마에 민트 향, 스파이시한 향이 더해지며 복합적인 향을 만들어낸다. 매끄럽게 다듬어진 타닌 맛을 즐길 수 있으며 그르나쉬 품종의 농밀한 과일 풍미가 입 안을 감싸고 시라 품종이 미들 팔렛을 채워주는 와인이다.', 2),
	(31, 'Calmel & Joseph, Les Terroirs Minervois', 'Chicken', 'Red', 1, 3, '시라/쉬라즈, 그르나슈, 까리냥', '서던 프랑스(Southern France) > 랑그독 루씨용(Languedoc Roussillon)', '체리 등의 붉은 과일 아로마가 풍부하게 나타나며 미네르부아 밭 인근에 자라고 있는 각종 허브, 덤불의 향과 다채로운 향신료 향이 오버랩된다. 입 안에서는 화사하고 진한 과일 풍미와 레드커런트처럼 새콤한 산미가 균형을 이루고 있으며 시나몬, 페퍼민트 등의 힌트가 여운으로 남는 와인이다.', 2),
	(32, 'Quinta da Raza, Avesso Alvarinho', 'Pasta', 'White', 1, 4, '아베소, 알바리뇨', '비뉴 베르데(Vinho Verde)', '과실향과 플로럴한 아로마가 인상적이다. 입 안에서는 다양하고 복합적인 풍미와 긴 여운을 자랑하는 강렬하고 산뜻한 스타일의 와인이다. 뛰어난 품질의 아베소와 알바리뉴를 블렌딩하여 좋은 숙성 잠재력을 지니고 있다.', 1),
	(33, 'Quinta da Raza, Avesso', 'Sweet Dessert', 'White', 1, 4, '아베소, 알바리뇨', '비뉴 베르데(Vinho Verde)', '과실향과 플로럴한 아로마가 인상적이다. 입 안에서는 다양하고 복합적인 풍미와 긴 여운을 자랑하는 강렬하고 산뜻한 스타일의 와인이다. 뛰어난 품질의 아베소와 알바리뉴를 블렌딩하여 좋은 숙성 잠재력을 지니고 있다.', 1),
	(34, 'Quinta da Raza, Alvarinho Trajadura', 'Pasta', 'White', 1, 4, '알바리뇨, 트라하두라', '비뉴 베르데(Vinho Verde)', '과실향과 플로럴한 아로마가 인상적이다. 다양하고 복합적인 풍미와 긴 여운을 자랑하며 강렬하고 산뜻한 스타일의 와인이다. 뛰어난 품질의 알바리뉴와 트라자두라를 블렌딩하여 좋은 숙성 잠재력을 지니고 있다.', 1),
	(35, 'Quinta da Raza, Dom Diogo Azal', 'Pasta', 'White', 1, 4, '아잘 블랑코', '비뉴 베르데(Vinho Verde)', '밝은 레몬색을 띠고 시트러스와 청사과가 두드러지는 기분 좋은 과실향이 난다. 입 안에서는 산도의 밸런스가 좋고 매우 신선하고 산뜻한 스타일의 와인이다.', 1),
	(36, 'Quinta da Raza, Dom Diogo Arinto', 'Sweet Dessert', 'White', 1, 4, '아린토', '비뉴 베르데(Vinho Verde)', '밝은 레몬색을 띠고 기분 좋은 과실향과 복합적인 풍미를 지녔다. 입 안에서는 오래도록 지속되는 산뜻한 맛이 인상적인 와인이다.', 1),
	(37, 'Burmester, White Port', 'Pork', 'White', 5, 2, '포트 블랜드', '도우루(Douro)', '선명한 감귤색을 보이고 아카시아 꿀 향, 진한 흰 꽃 아로마가 인상적이다. 입 안에서는 적당한 산미와 당도가 부드러운 목 넘김으로 이어지며 레드 포트에 비하여 덜 부담스럽게 접근할 수 있는 와인이다. 크림쉐리, 마르살라 보다 비교적 가볍게 마실 수 있다.', 1),
	(38, 'Burmester, Tavedo Rose', 'Cheese', 'Rose', 1, 3, '틴타 로리즈, 틴타 바로카, 틴타 아마렐라', '도우루(Douro)', '과실향과 플로럴한 아로마가 인상적이다. 다양하고 복합적인 풍미와 긴 여운을 자랑하며 강렬하고 산뜻한 스타일의 와인이다. 뛰어난 품질의 알바리뉴와 트라자두라를 블렌딩하여 좋은 숙성 잠재력을 지니고 있다.', 1),
	(39, 'Burmester, Tavedo Red', 'Beef', 'Fortified', 1, 3, '투리가 프란카, 틴타 로리즈, 틴타 까오, 틴타 바로카, 투리가 나시오날', '도우루(Douro)', '달콤한 라즈베리, 블랙 체리 등 붉은 과실류의 아로마와 초콜릿 풍미가 조화롭다. 어떤 음식과도 부담 없이 즐길 수 있는 와인이다.', 1),
	(40, 'Burmester, Sotto Voce Reserve Ruby Port', 'Lamb', 'Fortified', 5, 3, '투리가 나시오날, 투리가 프란카, 틴타 로리즈', '도우루(Douro)', '깊은 바이올렛 색을 보이며 진한 야생 베리 향, 농밀한 과일향이 전체적으로 감싼다. 입 안에서는 따뜻하고 벨벳처럼 부드러운 질감의 농축미와 적당한 타닌의 밸런스가 긴 여운으로 남는 와인이다.', 1),
	(41, 'Burmester, Tavedo White', 'Fish', 'White', 1, 4, '말바시아 피나, 고바이오, 라비가토, 폴가사오, 세르시알', '도우루(Douro)', '달콤한 허브, 꽃, 신선한 과일, 미네랄이 풍부하다. 입 안에서는 적당한 산미와 가벼운 바디가 입 안을 산뜻하게 하는 와인이다.', 1);
/*!40000 ALTER TABLE `wine_wine` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
