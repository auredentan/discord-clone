import React from 'react'

import { Avatar, VStack } from '@chakra-ui/react'

const Servers = () => {
	const servers = [{}, {}]
	return (
		<VStack spacing={4} align="stretch">
			{servers.map((server, idx) => {
				return (
					<Avatar
						key={idx}
						name="Dan Abrahmov"
						src="https://bit.ly/dan-abramov"
					/>
				)
			})}
		</VStack>
	)
}

export default Servers
