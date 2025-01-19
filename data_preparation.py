import pandas as pd

def prepare_data(historical_df):
    historical_df['topic'] = historical_df['quiz'].apply(lambda x: x.get('topic', 'Unknown'))
    historical_df['accuracy'] = historical_df.get('correct_answers', 0) / historical_df.get('total_questions', 1)
    historical_df['duration_minutes'] = (
        pd.to_datetime(historical_df['ended_at'], errors='coerce') -
        pd.to_datetime(historical_df['started_at'], errors='coerce')
    ).dt.total_seconds() / 60

    # Aggregate errors by topic
    topic_error_counts = historical_df.groupby('topic')['incorrect_answers'].sum().reset_index()
    topic_error_counts.columns = ['topic', 'error_count']

    # Merge to label weak topics
    historical_df = historical_df.merge(topic_error_counts, on='topic', how='left')
    historical_df['weak_topic'] = historical_df.apply(
        lambda x: x['topic'] if x['error_count'] > 0 else 'None', axis=1
    )

    features = historical_df[['score', 'accuracy', 'duration_minutes']]
    labels = historical_df['weak_topic']

    return features, labels
