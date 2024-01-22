# Flight booker


Creating a one-way flight booker.

# Setup

1. Search

    4 Dropdown menus to seach available flights
    - departure airport
    - arrival airport
    - date
    - number of passenger

    Creating Airport model
    - code (3 letters) + create seed to populate with airport data
    
    Creating Flight model
    - departure airport id
    - arrival airport id
    - start datetime
    - flight duration

    Seed database with flights

    /flights as root route

    Search form on the /flights index page using GET

    
2. Picking a flight

  - Showing the search results below
  - Rendering each search result with radio button
  - Add submit button (hidden field for number of passengers)

3. Passenger information

  - Creating Booking model
  - Creating Passenger model (name + email only)
  - Make associations between Bookings, Passengers and Flights
  - View getting flight id and passenger number parameters to render form which displays current date, airports, flight id and set of fields to enter personal information for each passenger