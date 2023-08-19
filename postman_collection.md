{
  "info": {
    "_postman_id": "bddba012-8c7a-475c-bb68-d2992b9ad423",
    "name": "API Endpoints",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Authorization",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"phone\": \"123-456-7890\"\n}"
        },
        "url": {
          "raw": "{{45.130.43.251:8000}}/auth/",
          "host": [
            "{{45.130.43.251:8000}}"
          ],
          "path": [
            "auth"
          ]
        }
      },
      "response": []
    },
    {
      "name": "Authenticate",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"phone\": \"998-456-7890\",\n  \"code\": \"1234\"\n}"
        },
        "url": {
          "raw": "{{45.130.43.251:8000}}/authenticate/",
          "host": [
            "{{45.130.43.251:8000}}"
          ],
          "path": [
            "code"
          ]
        }
      },
      "response": []
    },
    {
      "name": "ActivateInvite",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"user_id\": 1,\n  \"invite\": \"ABCD123\"\n}"
        },
        "url": {
          "raw": "{{45.130.43.251:8000}}/activate_invite/",
          "host": [
            "{{45.130.43.251:8000}}"
          ],
          "path": [
            "invite"
          ]
        }
      },
      "response": []
    },
    {
      "name": "GetUserDetail",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"user_id\": 1\n}"
        },
        "url": {
          "raw": "{{45.130.43.251:8000}}/get_user_detail/",
          "host": [
            "{{45.130.43.251:8000}}"
          ],
          "path": [
            "user"
          ]
        }
      },
      "response": []
    }
  ],
  "protocolProfileBehavior": {}
}
