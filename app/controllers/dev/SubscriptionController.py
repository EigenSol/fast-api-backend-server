
class SubscriptionController:

    @staticmethod
    async def list(request):
        return {
            "success": True,
            "subscriptions": [
                {
                    "code": "sub001",
                    "name": "Basic",
                    "trial_paymennt": 124.04, # None, 0, 124.24
                    "trial_duration_type": "days", # enum: days, months, years, weeeks
                    "trial_duration": 7,
                    "initial_payment": None, # None, 124.24
                    "recurring_interval": "month", # enum: month, year
                    "recurring_payment": 100,
                    "dynamic_payment": False, # True, False
                    "dynamic_description": '', # None, ''
                    "features": [
                        {
                            "label": "Feature 1",
                            "tooltip": "Hotel Assistant",
                            "is_included": True
                        },
                        {
                            "label": "Feature 2",
                            "tooltip": "Chat Plugin", # None
                            "is_included": False
                        }
                    ]
                }
            ]
        }
    