import __meta
import os.path
import datetime as dt
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class CalendarInstance:
    def __init__(self, credentials="./credentials.json"):
        self.SCOPES = ["https://www.googleapis.com/auth/calendar"]
        self.credentials = credentials
        self.connect()

    def connect(self, custom_token="token.json"):
        self.creds = None
        if os.path.exists(custom_token):
            self.creds = Credentials.from_authorized_user_file(custom_token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())

            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials, self.SCOPES
                )
                self.creds = flow.run_local_server(port=0)

            with open(custom_token, "w") as token:
                token.write(self.creds.to_json())

    def create_event(self, options: dict, get_link=False):
        try:
            service = build("calendar", "v3", credentials=self.creds)
            event = {
                "summary": options["summary"],
                "location": options["location"],
                "description": options["description"],
                "colorId": options["colorId"],
                "start": {
                    "dateTime": f"{options['date']}T{options['start_time']}+05:30",  # 2023-12-03 and 13:00:00 is the syntax
                    "timeZone": "Asia/Kolkata",
                },
                "end": {
                    "dateTime": f"{options['date']}T{options['end_time']}+05:30",
                    "timeZone": "Asia/Kolkata",
                },
                "recurrence": ["RRULE:FREQ=DAILY;COUNT=3"],
                "attendees": [{"email": "sarthakrawool09@gmail.com"}],
            }

            event = service.events().insert(calendarId="primary", body=event).execute()
            if get_link:
                print(f"Event Created: {event.get('htmllink')}")
            else:
                print("Event Created")

        except HttpError as error:
            print("An error has occurred", error)

    def find_calendar_id(self, calendar_name):
        calendars = self.get_all_calendars
        for calendar in calendars:
            name = calendar["summary"]
            if name.lower() == calendar_name.lower():
                id = calendar["id"]
                return id
            else:
                continue

    def read_calendar(
        self,
        calendar_id="primary",
        max_results=10,
        single_events=True,
        order_by="startTime",
    ):
        calendar_id = self.find_calendar_id(calendar_name=calendar_id)
        try:
            service = build("calendar", "v3", credentials=self.creds)
            now = dt.datetime.now().isoformat() + "Z"
            event_result = (
                service.events()
                .list(
                    calendarId=calendar_id,
                    timeMin=now,
                    maxResults=max_results,
                    singleEvents=single_events,
                    orderBy=order_by,
                )
                .execute()
            )
            events = event_result.get("items", [])

            if not events:
                print("No upcoming events")
                return

            data = pd.DataFrame(events)
            return data
            # for event in events:
            #     start = event['start'].get("dateTime", event['start'].get("date"))
            #     print(start, event['summary'])
        except HttpError as error:
            print("An error has occurred", error)

    @property
    def get_all_calendars(self):
        service = build("calendar", "v3", credentials=self.creds)
        calendars_result = service.calendarList().list().execute()
        calendars = calendars_result.get("items", [])
        return calendars


instance = CalendarInstance("../credentials.json")
