# CoWIN-Session

An app that looks for all available Covid Vaccine sessions available

## Setup

Clone the Repo

```bash
git clone https://github.com/Naik-Bharat/CoWIN-Session.git
```

Change Directories

```bash
cd CoWIN-Session/
```

Install requirements

```bash
pip3 install -r requirements.txt
```

Update information.json with your info

```json
{
    "state" : "Uttar Pradesh",
    "district" : "Ghaziabad",
    "date" : "16-03-2023",
    "age" : 18,
    "vaccine" : "COVISHIELD",
    "dose" : 2
}
```

## Run the script

```python
python3 main.py
```

Details of all slots where session is available is present in `available_sessions.json`