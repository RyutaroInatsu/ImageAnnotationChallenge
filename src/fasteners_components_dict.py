inserts_list = [
	['Tangless inserts', 'タングレスインサート'],
	['Thereaded inserts', 'ネジインサート'],
	['Tools for Tangless inserts', 'タングレスインサート専用工具'],
	['Tools for thereaded inserts', 'ネジインサート専用工具']
]

nuts_list = [
	['Cylindrical nuts', '丸ナット'],
	['Domed & Acorn nuts', '袋ナット'],
	['Flanged nuts', 'フランジ付ナット'],
	['Hex nuts', ' 六角ナット'],
	['High nuts(Spacers)', '高ナット(スペーサー)'],
	['Knurled nuts', 'ローレットナット'],
	['Lock nuts', 'ロックナット･ゆるみ止めナット'],
	['Non-metal nuts', '樹脂ナット'], # 要確認
	['Rectangular & Square nuts', '四角ナット'],
	['Wing nuts', '蝶ナット'],
	['Rivet nuts', 'リベットナット'],
	['Weld nuts', '溶接ナット'],
	['Clinching nuts', 'クリンチングナット'],
	['Clip nuts', 'クリップナット'],
	['Cap nuts', 'キャップナット'],
	['Washer based nuts', '歯付座金ナット･溝付六角ナット'],
	['Gauge nuts', 'ゲージナット'],
	['Screw plug hardware', 'スクリュープラグ'],
	['Shims', 'シム'],
	['Washers', '座金(ネジ用ワッシャ)']
]

screws_and_bolts_list = [
	['Captive washer screws', '座金組み込みネジ'],
	['Cross recessed bolts', '低頭ボルト'],
	['Eye screws, Eye bolts & Eye nuts', 'アイボルト･でんでんボルト'],
	['Fastener accessories', 'ネジ用アクセサリー'],
	['Fully-threaded bolts and Stud bolts', '全ネジ･スタッドボルト'],
	['Hex bolts', '六角ボルト'],
	['Hex socket button head cap screws', '六角付ボタンボルト'],
	['Hex socket flat head cap screws', '六角穴付皿ボルト'],
	['Hex socket head cap screws', '六角穴付ボルト'],
	['Micro screws and Precision screws', 'マイクロネジ･微細ネジ'],
	['Plastic and Ceramic screws', '樹脂ネジ･セラミックネジ'],
	['Self tapping screws', 'タッピングネジ･タップタイト･ハイテクネジ'],
	['Set screws', '止めネジ'],
	['Small head bolts', '小径ボルト'],
	['Space saving bolts', '低頭ボルト'],
	['Strippers, Reamers and Shoulder bolts', 'ストリッパー･リーマ･ショルダーボルト'],
	['Tamper resistant screws', 'いたずら防止ネジ'],
	['Vented screws', '貫通穴付ボルト'],
	['Wing, Thumb and Ornamental screws', '蝶ボルト･つまみネジ･化粧ビス']
]

shims_list = [
	['Rectangular shims', '角シム'],
	['Shim plates', 'シムプレート'],
	['Shim rings', 'シムリング'],
	['Shim tape', 'シムテープ']
]

washers_list = [
	['Metal washers', '金属ワッシャ'],
	['Non-metal washers and Collars', '非金属･樹脂ワッシャ']
]

fasteners_dict = {
	'Hand tools for screws' : ['Hand tools for screws', 'ネジ用工具'],
	'Hair pins and Cotter pins' : ['Hair pins and Cotter pins', 'スナップピン･割りピン'],
	'Inserts' :inserts_list,
	'Machine keys' : ['Machine keys', 'マシンキー'],
	'Nuts' : nuts_list,
	 'Retaining nuts' : ['Retaining nuts', '止め輪･リング'],
	'Screws and Bolts' : screws_and_bolts_list,
	 'Screws plug hardware': ['Screws plug hardware', 'スクリュープラグ'],
	'Shims' : shims_list,
	'Washers' : washers_list
}

if __name__ == '__main__':
	for item in fasteners_dict:
		print(f'Key is {item}. Values are {fasteners_dict[item]}')