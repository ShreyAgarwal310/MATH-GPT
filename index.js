import { Configuration, OpenAIApi } from "openai";
import { api_key } from './api_key.js';
import { organization } from './api_key.js';

const configuration = new Configuration({
    organization: organization,
    apiKey: api_key,
});

const openai = new OpenAIApi(Configuration);

const completion = await openai.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [
        {role: "user", content: "Hello World!"},
    ]
})

console.log(completion.data.choices[0].message);