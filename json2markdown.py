import json

def json_to_markdown_table(json_filepath, output_filepath=None):
    """
    JSONファイル（network-words.json）を読み込み、
    単語一覧をMarkdownの表形式で出力するスクリプト。
    """
    try:
        # JSONファイルの読み込み
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # JSONデータがリスト形式か辞書形式かチェック
        # 配列形式を想定（例: [{"word": "LAN", "reading": "ラン"}, ...]）
        if isinstance(data, dict):
            # もしトップレベルがオブジェクトで特定のキーにリストが入っている場合はここを調整
            # 例: data = data.get('words', [])
            words = data.values() if not isinstance(data, list) else data
        else:
            words = data

        if not words:
            print("データが見つかりませんでした。")
            return

        # surface（表記）で昇順ソート（大文字・小文字を区別せず並べ替え）
        words_sorted = sorted(
            words,
            key=lambda x: str(x.get("surface", "")).lower()
        )

        # 表のヘッダー定義（JSONのキーに合わせて適宜変更してください）
        # 例として word, reading, description などのキーを想定しています
        sample_item = words[0] if isinstance(words, list) else next(iter(words))
        headers = list(sample_item.keys()) if isinstance(sample_item, dict) else ["Value"]

        # Markdown表の構築
        markdown_lines = []
        
        # ヘッダー行と区切り行の作成
        header_row = "| " + " | ".join(str(h).capitalize() for h in headers) + " |"
        separator_row = "| " + " | ".join("---" for _ in headers) + " |"
        
        markdown_lines.append(header_row)
        markdown_lines.append(separator_row)

        # データ行の作成
        for item in words_sorted:
            if isinstance(item, dict):
                row = "| " + " | ".join(str(item.get(h, '')).replace('\n', ' ') for h in headers) + " |"
            else:
                row = f"| {str(item)} |"
            markdown_lines.append(row)

        markdown_output = "\n".join(markdown_lines)

        # 結果の出力
        if output_filepath:
            with open(output_filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_output)
            print(f"Markdown表を {output_filepath} に保存しました。")
        else:
            print(markdown_output)

    except FileNotFoundError:
        print(f"エラー: {json_filepath} が見つかりません。")
    except json.JSONDecodeError:
        print("エラー: JSONファイルの形式が正しくありません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    # 使用例: network-words.json を読み込み、output.md に保存する
    json_file = "network-words.json"
    # output_file = "network_words_table.md"
    
    #json_to_markdown_table(json_file, output_file)
    json_to_markdown_table(json_file)
