import axios from "axios";

export const API = axios.create({
	baseURL: "http://127.0.0.1:8000/",
	headers: {
		"Content-Type": "application/json",
	},
});

export const postMessage = (payload) => {
	return API.post(`messages/`, payload)
		.then((response) => response.data)
		.catch((error) => console.log(error));
};

export const deleteMessage = (msgId) => {
	return API.delete(`messages/${msgId}`)
		.then((response) => response.data)
		.catch((error) => console.log(error));
};
