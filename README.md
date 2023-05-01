# ChatGPT Plugins Examples

This repository contains examples of ChatGPT plugins that you can use as a starter code. 

* Stock and Crypto Price Plugin

## Stock and Crypto Price Plugin
This ChatGPT plugin allows you to fetch real-time stock and cryptocurrency prices directly within ChatGPT. With this plugin, you can easily inquire about the latest trading prices for popular stocks like Apple (AAPL) and cryptocurrencies like Bitcoin (BTC).

### Features

- Fetch real-time stock prices for publicly traded companies
- Fetch real-time cryptocurrency prices in USD
- Seamlessly integrate with ChatGPT to provide up-to-date market information

### Getting Started

To get started with this plugin, follow these steps:

First, start the FASTAPI server, which will get the Rest API for your plugin up and running. 
```
poetry install && poetry run dev 
```
The above will run the server at port 5000. 

Now, you are ready to install the plugin and start using it. 

Note, you would first need access to the developer preview of ChatGPT plugins, which you can apply for here:
* https://openai.com/waitlist/plugins 

From the front-end:
1. Install the plugin from the ChatGPT plugin store.
2. Once installed, you can start using the plugin by asking ChatGPT questions about stock and crypto prices. For example:
   - "What is the current price of Apple stock?"
   - "What is the current price of Bitcoin in USD?"

### Usage

Here are some example queries you can use with this plugin:

- "Where is Tesla trading at?"
- "What is the current price of ETH/USD?"
- "How much is Amazon stock worth right now?"

### Contributing

We welcome contributions to this plugin! If you have any ideas for improvements or new features, please feel free to open an issue or submit a pull request.

### License

This plugin is licensed under the [MIT License](LICENSE).

### Contact

For any questions or support, please contact us at [public@nextword.dev](mailto:public@nextword.dev).
