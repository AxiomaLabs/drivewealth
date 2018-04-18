from ..schemas import create_object_from_json_response


class UserApiMixin:
    """
    Details specific user
    """

    def get_user(self, user_id):
        """
        Get user's information
        @Params
            user_id: User id String
        @Return
            User Object
        """
        response = self.drive_wealth.users(self.user_id).GET()
        return create_object_from_json_response('User', response)

    def get_account_performance(self, user_id, account_id):
        """
        Provides daily realized and unrealized PL for a specific account
        @Params
            userID required
            accountID required
            dateRange string
                Used for specific date range, accepts a start and end date.
                See startDate and endDate query params for usage.
            history string
                Used for relative date range, accepts a number and a unit of
                time. See period query param for usage.
        @return object
            accountID
            accountNo
            lastUpdated
            performance [
                {
                  realizedDayPL
                  unrealizedDayPL
                  cumRealizedPL
                  date
                  equity
                  cash
                  deposits
                  withdrawals
                  fees
                }
            ]
        """
        response = self.drive_wealth.users(user_id).accountPerformance(
            account_id).GET()
        return create_object_from_json_response('AccountPerformance', response)
