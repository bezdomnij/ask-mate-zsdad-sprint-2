import csv
DATA_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time',  'vote_number', 'question_id', 'message', 'image']


def get_max_id(datalist):
    sorted_stuff = sorting(datalist, sortkey='id', rev=True)
    return sorted_stuff[0]['id']


def get_data(filename):
    all_data = []
    with open("sample_data/" + filename, mode='r') as questions:
        question_reader = csv.DictReader(questions)
        for i in question_reader:
            all_data.append(i)
    return all_data


def sorting(datalist, sortkey, rev=False):
    return sorted(datalist, key=lambda x: x[sortkey], reverse=rev)


def send_data(filename, questions):
    with open("sample_data/" + filename, mode='w') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for question in questions:
            writer.writerow({'id': question['id'],
                             'submission_time': question['submission_time'],
                             'vote_number': question['vote_number'],
                             'title': question['title'],
                             'message': question['message'],
                             'image': question['image']})


def send_answers(filename, questions):
    with open("sample_data/" + filename, mode='w') as csvfile:
        fieldnames = ANSWER_HEADER
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for question in questions:
            writer.writerow({'id': question['id'],
                             'submission_time': question['submission_time'],
                             'vote_number': question['vote_number'],
                             'question_id': question['question_id'],
                             'message': question['message'],
                             'image': question['image']})


def main():
    qlist = get_data('question.csv')
    get_max_id(qlist)


if __name__ == "__main__":
    main()
