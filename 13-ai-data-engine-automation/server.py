# server.py
from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta
import json

# Create an MCP server for Data Automation
mcp = FastMCP("DataAutomation")

# Mock data representing work tech information
CHAT_MESSAGES = [
    {"id": 1, "timestamp": "2025-08-26 09:15:00", "platform": "Microsoft Teams", "user": "Alice Johnson", "channel": "Project Alpha", "content": "Can we schedule the design review for next week?", "sentiment": "neutral", "keywords": ["design", "review", "schedule"]},
    {"id": 2, "timestamp": "2025-08-26 10:30:00", "platform": "Microsoft Teams", "user": "Bob Smith", "channel": "Project Alpha", "content": "The API integration is complete and ready for testing", "sentiment": "positive", "keywords": ["API", "integration", "testing", "complete"]},
    {"id": 3, "timestamp": "2025-08-26 11:45:00", "platform": "Slack", "user": "Carol Davis", "channel": "Engineering", "content": "Having issues with the database connection in production", "sentiment": "negative", "keywords": ["database", "connection", "production", "issues"]},
    {"id": 4, "timestamp": "2025-08-26 14:20:00", "platform": "Microsoft Teams", "user": "David Wilson", "channel": "Marketing", "content": "Great work on the Q3 campaign results! Exceeded expectations", "sentiment": "positive", "keywords": ["Q3", "campaign", "results", "exceeded", "expectations"]},
    {"id": 5, "timestamp": "2025-08-26 15:10:00", "platform": "Discord", "user": "Eve Brown", "channel": "Design Team", "content": "Need feedback on the new UI mockups by end of week", "sentiment": "neutral", "keywords": ["feedback", "UI", "mockups", "deadline"]}
]

EMAIL_DATA = [
    {"id": 1, "timestamp": "2025-08-26 08:00:00", "sender": "manager@company.com", "subject": "Weekly Team Standup", "platform": "Outlook", "priority": "normal", "content": "Reminder about our weekly standup meeting tomorrow at 10 AM", "keywords": ["standup", "meeting", "reminder"]},
    {"id": 2, "timestamp": "2025-08-26 12:15:00", "sender": "client@external.com", "subject": "Project Milestone Review", "platform": "Outlook", "priority": "high", "content": "Please provide status update on the current project milestones", "keywords": ["milestone", "review", "status", "update"]},
    {"id": 3, "timestamp": "2025-08-26 16:30:00", "sender": "hr@company.com", "subject": "Training Session Announcement", "platform": "Gmail", "priority": "low", "content": "New training sessions available for professional development", "keywords": ["training", "professional", "development"]},
]

DOCUMENTS = [
    {"id": 1, "name": "Project_Alpha_Requirements.docx", "created": "2025-08-20", "platform": "SharePoint", "author": "Alice Johnson", "type": "requirements", "content": "Project requirements document outlining technical specifications and user stories", "keywords": ["requirements", "specifications", "user stories"]},
    {"id": 2, "name": "Q3_Performance_Report.xlsx", "created": "2025-08-25", "platform": "OneDrive", "author": "David Wilson", "type": "report", "content": "Quarterly performance metrics and KPI analysis", "keywords": ["performance", "metrics", "KPI", "quarterly"]},
    {"id": 3, "name": "Design_Mockups_v2.pptx", "created": "2025-08-24", "platform": "SharePoint", "author": "Eve Brown", "type": "presentation", "content": "Updated UI/UX design mockups for the new application", "keywords": ["design", "mockups", "UI", "UX", "application"]},
]

MEETING_RECORDINGS = [
    {"id": 1, "title": "Project Alpha Kickoff", "date": "2025-08-20", "duration": "45 minutes", "platform": "Microsoft Teams", "participants": ["Alice Johnson", "Bob Smith", "Carol Davis"], "transcript": "Discussion about project scope, timeline, and resource allocation", "keywords": ["kickoff", "scope", "timeline", "resources"]},
    {"id": 2, "title": "Weekly Engineering Sync", "date": "2025-08-23", "duration": "30 minutes", "platform": "Zoom", "participants": ["Bob Smith", "Carol Davis", "Eve Brown"], "transcript": "Technical discussions about API integration and database optimization", "keywords": ["engineering", "API", "database", "optimization"]},
    {"id": 3, "title": "Client Presentation", "date": "2025-08-25", "duration": "60 minutes", "platform": "Microsoft Teams", "participants": ["David Wilson", "Alice Johnson"], "transcript": "Presentation of Q3 results and future roadmap discussion", "keywords": ["presentation", "Q3", "results", "roadmap"]},
]

@mcp.tool()
def ingest_chat_messages(platform: str = None, days_back: int = 7) -> dict:
    """Ingest and analyze chat messages from work collaboration platforms like Teams, Slack, Discord."""
    filtered_messages = CHAT_MESSAGES
    
    if platform:
        filtered_messages = [msg for msg in filtered_messages if msg["platform"].lower() == platform.lower()]
    
    # Simulate filtering by date
    cutoff_date = datetime.now() - timedelta(days=days_back)
    
    return {
        "total_messages": len(filtered_messages),
        "platforms": list(set([msg["platform"] for msg in filtered_messages])),
        "messages": filtered_messages,
        "sentiment_analysis": {
            "positive": len([msg for msg in filtered_messages if msg["sentiment"] == "positive"]),
            "negative": len([msg for msg in filtered_messages if msg["sentiment"] == "negative"]),
            "neutral": len([msg for msg in filtered_messages if msg["sentiment"] == "neutral"])
        }
    }

@mcp.tool()
def ingest_email_data(priority: str = None, days_back: int = 7) -> dict:
    """Ingest and analyze email data from Outlook, Gmail, and other email platforms."""
    filtered_emails = EMAIL_DATA
    
    if priority:
        filtered_emails = [email for email in filtered_emails if email["priority"].lower() == priority.lower()]
    
    return {
        "total_emails": len(filtered_emails),
        "platforms": list(set([email["platform"] for email in filtered_emails])),
        "emails": filtered_emails,
        "priority_breakdown": {
            "high": len([email for email in filtered_emails if email["priority"] == "high"]),
            "normal": len([email for email in filtered_emails if email["priority"] == "normal"]),
            "low": len([email for email in filtered_emails if email["priority"] == "low"])
        }
    }

@mcp.tool()
def ingest_documents(document_type: str = None, platform: str = None) -> dict:
    """Ingest and analyze documents from SharePoint, OneDrive, Google Drive, and other document platforms."""
    filtered_docs = DOCUMENTS
    
    if document_type:
        filtered_docs = [doc for doc in filtered_docs if doc["type"].lower() == document_type.lower()]
    
    if platform:
        filtered_docs = [doc for doc in filtered_docs if doc["platform"].lower() == platform.lower()]
    
    return {
        "total_documents": len(filtered_docs),
        "platforms": list(set([doc["platform"] for doc in filtered_docs])),
        "document_types": list(set([doc["type"] for doc in filtered_docs])),
        "documents": filtered_docs
    }

@mcp.tool()
def ingest_meeting_recordings(platform: str = None, days_back: int = 30) -> dict:
    """Ingest and analyze meeting recordings and transcripts from Teams, Zoom, and other platforms."""
    filtered_meetings = MEETING_RECORDINGS
    
    if platform:
        filtered_meetings = [meeting for meeting in filtered_meetings if meeting["platform"].lower() == platform.lower()]
    
    return {
        "total_meetings": len(filtered_meetings),
        "platforms": list(set([meeting["platform"] for meeting in filtered_meetings])),
        "total_participants": len(set([participant for meeting in filtered_meetings for participant in meeting["participants"]])),
        "meetings": filtered_meetings
    }

@mcp.tool()
def search_work_data(query: str, data_types: list = None) -> dict:
    """Search across all ingested work tech data using keywords or content search."""
    if data_types is None:
        data_types = ["chat", "email", "documents", "meetings"]
    
    results = {
        "query": query,
        "results": []
    }
    
    query_lower = query.lower()
    
    # Search chat messages
    if "chat" in data_types:
        for msg in CHAT_MESSAGES:
            if query_lower in msg["content"].lower() or any(keyword.lower() in query_lower for keyword in msg["keywords"]):
                results["results"].append({
                    "type": "chat_message",
                    "platform": msg["platform"],
                    "relevance_score": 0.9,
                    "data": msg
                })
    
    # Search emails
    if "email" in data_types:
        for email in EMAIL_DATA:
            if query_lower in email["content"].lower() or query_lower in email["subject"].lower():
                results["results"].append({
                    "type": "email",
                    "platform": email["platform"],
                    "relevance_score": 0.8,
                    "data": email
                })
    
    # Search documents
    if "documents" in data_types:
        for doc in DOCUMENTS:
            if query_lower in doc["content"].lower() or any(keyword.lower() in query_lower for keyword in doc["keywords"]):
                results["results"].append({
                    "type": "document",
                    "platform": doc["platform"],
                    "relevance_score": 0.85,
                    "data": doc
                })
    
    # Search meeting recordings
    if "meetings" in data_types:
        for meeting in MEETING_RECORDINGS:
            if query_lower in meeting["transcript"].lower() or any(keyword.lower() in query_lower for keyword in meeting["keywords"]):
                results["results"].append({
                    "type": "meeting_recording",
                    "platform": meeting["platform"],
                    "relevance_score": 0.75,
                    "data": meeting
                })
    
    # Sort by relevance score
    results["results"] = sorted(results["results"], key=lambda x: x["relevance_score"], reverse=True)
    results["total_results"] = len(results["results"])
    
    return results

@mcp.tool()
def get_collaboration_insights() -> dict:
    """Get insights and analytics about collaboration patterns from ingested work tech data."""
    
    # Calculate collaboration metrics
    all_participants = set()
    platform_usage = {}
    content_categories = {}
    
    # Analyze chat data
    for msg in CHAT_MESSAGES:
        all_participants.add(msg["user"])
        platform = msg["platform"]
        platform_usage[platform] = platform_usage.get(platform, 0) + 1
        
        for keyword in msg["keywords"]:
            content_categories[keyword] = content_categories.get(keyword, 0) + 1
    
    # Analyze meeting data
    for meeting in MEETING_RECORDINGS:
        for participant in meeting["participants"]:
            all_participants.add(participant)
        platform = meeting["platform"]
        platform_usage[platform] = platform_usage.get(platform, 0) + 1
    
    # Most active platforms
    top_platforms = sorted(platform_usage.items(), key=lambda x: x[1], reverse=True)
    
    # Most discussed topics
    top_topics = sorted(content_categories.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return {
        "total_active_users": len(all_participants),
        "active_users": list(all_participants),
        "platform_usage": dict(top_platforms),
        "top_discussion_topics": dict(top_topics),
        "collaboration_summary": {
            "total_interactions": len(CHAT_MESSAGES) + len(EMAIL_DATA) + len(MEETING_RECORDINGS),
            "platforms_in_use": len(platform_usage),
            "document_repositories": len(set([doc["platform"] for doc in DOCUMENTS]))
        }
    }

@mcp.tool()
def extract_action_items(data_type: str = "all") -> dict:
    """Extract action items and tasks from ingested work tech data using AI analysis."""
    action_items = []
    
    # Analyze chat messages for action items
    if data_type in ["all", "chat"]:
        for msg in CHAT_MESSAGES:
            if any(word in msg["content"].lower() for word in ["schedule", "need", "deadline", "complete", "review"]):
                action_items.append({
                    "source": "chat",
                    "platform": msg["platform"],
                    "assignee": "TBD",
                    "description": msg["content"],
                    "priority": "medium",
                    "extracted_from": f"{msg['user']} in {msg['channel']}",
                    "timestamp": msg["timestamp"]
                })
    
    # Analyze emails for action items
    if data_type in ["all", "email"]:
        for email in EMAIL_DATA:
            if any(word in email["content"].lower() for word in ["please", "update", "provide", "review"]):
                action_items.append({
                    "source": "email",
                    "platform": email["platform"],
                    "assignee": "TBD",
                    "description": email["content"],
                    "priority": email["priority"],
                    "extracted_from": f"Email from {email['sender']}",
                    "timestamp": email["timestamp"]
                })
    
    # Analyze meeting recordings for action items
    if data_type in ["all", "meetings"]:
        for meeting in MEETING_RECORDINGS:
            if any(word in meeting["transcript"].lower() for word in ["action", "follow up", "next steps", "assign"]):
                action_items.append({
                    "source": "meeting",
                    "platform": meeting["platform"],
                    "assignee": "TBD",
                    "description": f"Follow up from: {meeting['transcript']}",
                    "priority": "medium",
                    "extracted_from": f"Meeting: {meeting['title']}",
                    "timestamp": meeting["date"]
                })
    
    return {
        "total_action_items": len(action_items),
        "action_items": action_items,
        "breakdown_by_source": {
            "chat": len([item for item in action_items if item["source"] == "chat"]),
            "email": len([item for item in action_items if item["source"] == "email"]),
            "meetings": len([item for item in action_items if item["source"] == "meeting"])
        }
    }

mcp.run()
