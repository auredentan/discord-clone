import React, { useState } from 'react'

import { Avatar, Stack, Text } from '@chakra-ui/react'

import { ChatMessage, User } from 'types/chat'
import { ChatMessageContent } from './ChatMessageContent'
import { ChatMessageActionBar } from './ChatMessageActionBar'

export interface ChatMessageCardProps {
	user: User
	message: ChatMessage
}

export const ChatMessageCard = ({ user, message }: ChatMessageCardProps) => {
	const [isHightlighted, setIsHightlighted] = useState(false)
	return (
		<Stack
			direction={['row']}
			spacing="24px"
			isInline
			borderWidth="2px"
			backgroundColor={isHightlighted ? 'gray.700' : 'brand'}
			onMouseEnter={() => setIsHightlighted(true)}
			onMouseLeave={() => setIsHightlighted(false)}
			position="relative"
		>
			{/* Actions */}
			{isHightlighted && <ChatMessageActionBar />}

			{/* Profile column */}
			<Stack direction={['column']} alignItems="center">
				<Avatar size="lg" name={user.name} src={user.picture} loading="lazy" />
			</Stack>

			{/* Message column */}
			<Stack direction={['column']}>
				{/* Title */}
				<Stack direction={['row']} spacing="16px">
					<Text fontSize="lg" color="green" fontWeight="bold" as="div">
						{user.name}
						<Text marginLeft="0.25rem" fontSize="md" color="gray.500" as="span">
							{message.date}
						</Text>
					</Text>
				</Stack>

				{/* Message */}
				<ChatMessageContent message={message} />
			</Stack>
		</Stack>
	)
}
