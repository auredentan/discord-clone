import React from 'react'

import { Stack } from '@chakra-ui/react'

import { ChatMessageCard } from '../ChatMessageCard'

const Chat = () => {
	const messages = [
		{
			message: 'Message',
			date: '2020',
			emojis: [
				'https://emojiapi.dev/api/v1/face_with_tears_of_joy.svg',
				'https://emojiapi.dev/api/v1/pleading_face.svg',
			],
		},
		{
			message: 'Message',
			date: '2020',
			emojis: [
				'https://emojiapi.dev/api/v1/face_with_tears_of_joy.svg',
				'https://emojiapi.dev/api/v1/pleading_face.svg',
			],
		},
	]
	const user = {
		name: 'User',
		picture: 'https://bit.ly/dan-abramov',
	}
	return (
		<Stack direction={['column']} spacing="24px">
			{messages.map((message, index) => (
				<ChatMessageCard key={index} user={user} message={message} />
			))}
		</Stack>
	)
}

export default Chat
