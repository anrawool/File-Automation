from googleapiclient.discovery import build
from PvtInfo import info

# Set your API key obtained from Google Cloud Platform
API_KEY = info.Google_Token

# Function to search YouTube and get video titles and URLs
def search_youtube(query, max_results=1):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=max_results
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        video_title = search_result['snippet']['title']
        video_id = search_result['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        videos.append({'title': video_title, 'url': video_url})

    return videos

# Example usage
if __name__ == "__main__":
    search_query = input("Enter your YouTube search query: ")
    search_results = search_youtube(search_query)

    print("Search Results:")
    for idx, result in enumerate(search_results, start=1):
        print(f"{idx}. {result['title']} - {result['url']}")
