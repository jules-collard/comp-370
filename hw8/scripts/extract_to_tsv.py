import argparse, csv, json, random

def write_dict_to_tsv(data, tsv_path):
    with open(tsv_path, "w") as tsv_out:
        tsv_writer = csv.writer(tsv_out, delimiter='\t')
        tsv_writer.writerow(data[0].keys())
        for row in data:
            tsv_writer.writerow(row.values())

def extract_posts(dict):
    posts = dict["data"]["children"]
    data = [{
        "name":post["data"]["name"],
        "title":post["data"]["title"],
        "coding":""
    } for post in posts]
    return data

def main():
    parser = argparse.ArgumentParser(
        prog="json_to_tsv",
        description="Writes JSON file into TSV format"
    )
    parser.add_argument("--out_file", "-o", required=True,help="Output File Path")
    parser.add_argument("json_file",help="Input JSON file path")
    parser.add_argument("num_posts_to_output", help="Number of posts to output")
    args = parser.parse_args()

    with open(args.json_file, "r") as f:
        data = json.load(f)
    
    posts = extract_posts(data)
    write_dict_to_tsv(random.sample(posts, min(int(args.num_posts_to_output), len(posts))), args.out_file)

if __name__ == "__main__":
    main()


