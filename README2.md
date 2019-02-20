# Trading AI

A cryptocurrency trading software currently in development.

## Getting Started

Launch contents of balanceViewer in a Python IDE.

### Prerequisites

A binance account is needed to use this software.

<b>Follow the link below to create an account if you don't already have one:</b>

    https://www.binance.com/?ref=16527883
    
 After logging into Binance, follow the following steps to create your API keys:
    
    1. Navigate to your account settings
    2. Select API Setting and enter a name for your API key label
    3. Save your secret key and your api key in a safe location
    4. Your secret key will only be viewable once, so ensure you have a copy of this
    5. Ensure the following options are enabled:
      [x] Read info
      [x] Enable trading
      [x] Enable withdrawals
    6. Select the option "Restrict access to trusted IPs only" and enter your IP address
    7. Save changes

### Setup

After initializing API keys, enter them into lines 7 and 8 of balanceViewer.py

```
api_secret = 'enter secret key here'
api_key = 'enter key here'
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
