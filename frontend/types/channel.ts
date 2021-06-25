export interface Channel {
	id: string
	name: string
	type: ChannelType
	category: ChannelCategory
}

export interface ChannelCategory {
	id: string
	name: string
}

export enum ChannelType {
	text = 'text',
	vocal = 'vocal',
}
